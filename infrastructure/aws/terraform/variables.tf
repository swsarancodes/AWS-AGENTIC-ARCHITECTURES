variable "aws_region" {
  description = "AWS Region"
  default     = "us-east-1"
}

variable "bedrock_model_id" {
  description = "Bedrock Model ID"
  default     = "anthropic.claude-3-sonnet-20240229-v1:0"
}
