from patterns.base.agent_base import AgentBase
from patterns.base.bedrock_client import BedrockClient
from tools.currency_tool import CurrencyTool
from tools.web_search_tool import WebSearchTool

class ToolUsingAgent(AgentBase):
    """
    Tool-using agent that integrates external tools with AWS Bedrock LLM.
    """
    def __init__(self, config):
        super().__init__(config)
        self.bedrock = BedrockClient(region=config.get("region"))
        self.model_id = config.get("model_id", "anthropic.claude-3-sonnet-20240229-v1:0")
        self.tools = {
            "currency": CurrencyTool(),
            "web_search": WebSearchTool(config),
        }

    def run(self, input_data):
        prompt = f"Use available tools to answer: {input_data}"
        response = self.bedrock.invoke_model(self.model_id, prompt)
        return self._process_with_tools(response)

    def _process_with_tools(self, response):
        # Simple tool invocation logic
        if "currency" in response.lower():
            return self.tools["currency"].execute({})
        elif "search" in response.lower():
            return self.tools["web_search"].execute({"query": "example"})
        return response

    def get_config(self):
        return self.config
