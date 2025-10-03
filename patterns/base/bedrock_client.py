import boto3
import os
import json
import time
import logging
from typing import Dict, Any, Optional, Iterator, List
from botocore.exceptions import ClientError, BotoCoreError
from botocore.config import Config

logger = logging.getLogger(__name__)


class BedrockClientError(Exception):
    pass


class BedrockClient:
    
    CLAUDE_3_OPUS = "anthropic.claude-3-opus-20240229-v1:0"
    CLAUDE_3_SONNET = "anthropic.claude-3-sonnet-20240229-v1:0"
    CLAUDE_3_HAIKU = "anthropic.claude-3-haiku-20240307-v1:0"
    TITAN_EMBED_G1 = "amazon.titan-embed-text-v1"
    TITAN_EMBED_V2 = "amazon.titan-embed-text-v2:0"
    
    def __init__(self, 
                 region: Optional[str] = None,
                 max_retries: int = 3,
                 timeout: int = 300):
        self.region = region or os.getenv("AWS_REGION", "us-east-1")
        self.max_retries = max_retries
        self.timeout = timeout
        
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.request_count = 0
        
        config = Config(
            region_name=self.region,
            retries={'max_attempts': max_retries, 'mode': 'adaptive'},
            connect_timeout=timeout,
            read_timeout=timeout
        )
        
        try:
            self.client = boto3.client("bedrock-runtime", config=config)
            self.bedrock_client = boto3.client("bedrock", config=config)
            logger.info(f"BedrockClient initialized for region: {self.region}")
        except Exception as e:
            logger.error(f"Failed to initialize Bedrock client: {e}")
            raise BedrockClientError(f"Client initialization failed: {e}")
    
    def invoke_model(self,
                    model_id: str,
                    prompt: str,
                    max_tokens: int = 4096,
                    temperature: float = 0.7,
                    top_p: float = 0.9,
                    top_k: int = 250,
                    stop_sequences: Optional[List[str]] = None,
                    system_prompt: Optional[str] = None) -> Dict[str, Any]:
        
        try:

            if "claude-3" in model_id:
                body = self._build_claude3_request(
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                    stop_sequences=stop_sequences,
                    system_prompt=system_prompt
                )
            else:
                body = self._build_claude_request(
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                    stop_sequences=stop_sequences
                )

            start_time = time.time()
            response = self.client.invoke_model(
                modelId=model_id,
                contentType="application/json",
                accept="application/json",
                body=json.dumps(body)
            )
            
            execution_time = time.time() - start_time

            response_body = json.loads(response['body'].read().decode())

            if "claude-3" in model_id:
                completion = response_body['content'][0]['text']
                stop_reason = response_body.get('stop_reason', 'unknown')
            else:
                completion = response_body.get('completion', '')
                stop_reason = response_body.get('stop_reason', 'unknown')

            input_tokens = response_body.get('usage', {}).get('input_tokens', 0)
            output_tokens = response_body.get('usage', {}).get('output_tokens', 0)
            
            self.total_input_tokens += input_tokens
            self.total_output_tokens += output_tokens
            self.request_count += 1
            
            logger.info(
                f"Model invoked: {model_id}, "
                f"input_tokens={input_tokens}, output_tokens={output_tokens}, "
                f"time={execution_time:.2f}s"
            )
            
            return {
                "completion": completion,
                "stop_reason": stop_reason,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "model_id": model_id,
                "execution_time": execution_time,
                "full_response": response_body
            }
            
        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_message = e.response['Error']['Message']
            logger.error(f"Bedrock API error: {error_code} - {error_message}")
            raise BedrockClientError(f"API error: {error_code} - {error_message}")
        except Exception as e:
            logger.error(f"Unexpected error invoking model: {e}")
            raise BedrockClientError(f"Model invocation failed: {e}")
    
    def invoke_model_stream(self,
                           model_id: str,
                           prompt: str,
                           **kwargs) -> Iterator[str]:
        
        try:
            body = self._build_claude3_request(prompt=prompt, **kwargs)
            
            response = self.client.invoke_model_with_response_stream(
                modelId=model_id,
                contentType="application/json",
                accept="application/json",
                body=json.dumps(body)
            )
            
            stream = response.get('body')
            if stream:
                for event in stream:
                    chunk = event.get('chunk')
                    if chunk:
                        chunk_data = json.loads(chunk.get('bytes').decode())
                        if 'delta' in chunk_data:
                            delta_text = chunk_data['delta'].get('text', '')
                            if delta_text:
                                yield delta_text
                                
        except Exception as e:
            logger.error(f"Streaming error: {e}")
            raise BedrockClientError(f"Streaming failed: {e}")
    
    def embed_text(self,
                   text: str,
                   model_id: Optional[str] = None) -> List[float]:
        
        model_id = model_id or self.TITAN_EMBED_V2
        
        try:
            body = json.dumps({"inputText": text})
            
            response = self.client.invoke_model(
                modelId=model_id,
                contentType="application/json",
                accept="application/json",
                body=body
            )
            
            response_body = json.loads(response['body'].read().decode())
            embedding = response_body.get('embedding', [])
            
            logger.debug(f"Generated embedding of dimension {len(embedding)}")
            return embedding
            
        except Exception as e:
            logger.error(f"Embedding generation failed: {e}")
            raise BedrockClientError(f"Embedding failed: {e}")
    
    def _build_claude3_request(self, prompt: str, **kwargs) -> Dict[str, Any]:
        
        messages = [{"role": "user", "content": prompt}]
        
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "messages": messages,
            "max_tokens": kwargs.get('max_tokens', 4096),
            "temperature": kwargs.get('temperature', 0.7),
            "top_p": kwargs.get('top_p', 0.9),
            "top_k": kwargs.get('top_k', 250)
        }
        
        if kwargs.get('system_prompt'):
            body['system'] = kwargs['system_prompt']
        
        if kwargs.get('stop_sequences'):
            body['stop_sequences'] = kwargs['stop_sequences']
        
        return body
    
    def _build_claude_request(self, prompt: str, **kwargs) -> Dict[str, Any]:
        
        return {
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens_to_sample": kwargs.get('max_tokens', 4096),
            "temperature": kwargs.get('temperature', 0.7),
            "top_p": kwargs.get('top_p', 0.9),
            "top_k": kwargs.get('top_k', 250),
            "stop_sequences": kwargs.get('stop_sequences', ["\n\nHuman:"])
        }
    
    def get_usage_stats(self) -> Dict[str, Any]:
        
        return {
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "request_count": self.request_count,
            "average_input_tokens": self.total_input_tokens / max(self.request_count, 1),
            "average_output_tokens": self.total_output_tokens / max(self.request_count, 1)
        }
    
    def reset_usage_stats(self) -> None:
        
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.request_count = 0
        logger.info("Usage statistics reset")
    
    def list_available_models(self) -> List[Dict[str, Any]]:
        
        try:
            response = self.bedrock_client.list_foundation_models()
            models = response.get('modelSummaries', [])
            logger.info(f"Found {len(models)} available models")
            return models
        except Exception as e:
            logger.error(f"Failed to list models: {e}")
            return []
    
    def __repr__(self) -> str:
        return f"BedrockClient(region='{self.region}', requests={self.request_count})"


