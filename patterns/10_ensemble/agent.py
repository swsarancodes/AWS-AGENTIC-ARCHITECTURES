"""Ensemble pattern."""
from patterns.base.agent_base import AgentBase

class EnsembleAgent(AgentBase):
    """Aggregates outputs from multiple models."""
    def __init__(self, config):
        super().__init__(config)
        self.models = ["model1", "model2", "model3"]

    def run(self, input_data):
        outputs = [f"{model}: {input_data}" for model in self.models]
        return self._aggregate(outputs)

    def _aggregate(self, outputs):
        return f"Ensemble result: {outputs}"

    def get_config(self):
        return self.config
