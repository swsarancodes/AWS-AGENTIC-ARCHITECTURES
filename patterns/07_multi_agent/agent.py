"""Multi-Agent pattern."""
from patterns.base.agent_base import AgentBase
from patterns.base.bedrock_client import BedrockClient

class MultiAgentSystem(AgentBase):
    """Coordinates multiple specialized agents."""
    def __init__(self, config):
        super().__init__(config)
        self.bedrock = BedrockClient(region=config.get("region"))
        self.agents = self._initialize_agents()

    def _initialize_agents(self):
        return {"analyst": "Agent1", "researcher": "Agent2"}

    def run(self, input_data):
        results = {name: f"{name} processed {input_data}" for name in self.agents}
        return self._aggregate(results)

    def _aggregate(self, results):
        return f"Aggregated: {results}"

    def get_config(self):
        return self.config
