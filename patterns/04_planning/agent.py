from patterns.base.agent_base import AgentBase
from patterns.base.bedrock_client import BedrockClient

class PlanningAgent(AgentBase):
    """Planning agent that creates structured plans before execution."""
    def __init__(self, config):
        super().__init__(config)
        self.bedrock = BedrockClient(region=config.get("region"))
        self.model_id = config.get("model_id", "anthropic.claude-3-sonnet-20240229-v1:0")

    def run(self, input_data):
        plan = self._create_plan(input_data)
        result = self._execute_plan(plan)
        return result

    def _create_plan(self, input_data):
        prompt = f"Create a step-by-step plan for: {input_data}"
        return self.bedrock.invoke_model(self.model_id, prompt)

    def _execute_plan(self, plan):
        return f"Executed plan: {plan}"

    def get_config(self):
        return self.config
