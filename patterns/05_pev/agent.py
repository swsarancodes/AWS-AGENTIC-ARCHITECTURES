from patterns.base.agent_base import AgentBase
from patterns.base.bedrock_client import BedrockClient

class PEVAgent(AgentBase):
    """Plan-Execute-Verify agent for robust task execution."""
    def __init__(self, config):
        super().__init__(config)
        self.bedrock = BedrockClient(region=config.get("region"))
        self.model_id = config.get("model_id", "anthropic.claude-3-sonnet-20240229-v1:0")

    def run(self, input_data):
        plan = self._plan(input_data)
        result = self._execute(plan)
        verified = self._verify(result)
        return verified

    def _plan(self, input_data):
        return f"Plan for {input_data}"

    def _execute(self, plan):
        return f"Executed {plan}"

    def _verify(self, result):
        return f"Verified {result}"

    def get_config(self):
        return self.config
