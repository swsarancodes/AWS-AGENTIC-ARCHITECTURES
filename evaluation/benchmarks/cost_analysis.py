class CostAnalysis:
    """Cost analysis for AWS Bedrock usage."""
    def __init__(self):
        self.pricing = {
            "anthropic.claude-3-sonnet-20240229-v1:0": {"input": 0.003, "output": 0.015},
            "anthropic.claude-3-haiku-20240307-v1:0": {"input": 0.00025, "output": 0.00125}
        }
    
    def calculate_cost(self, model_id, input_tokens, output_tokens):
        if model_id not in self.pricing:
            return {"error": "Model not found"}
        
        pricing = self.pricing[model_id]
        cost = (input_tokens / 1000) * pricing["input"] + (output_tokens / 1000) * pricing["output"]
        return {"cost_usd": cost, "input_tokens": input_tokens, "output_tokens": output_tokens}
