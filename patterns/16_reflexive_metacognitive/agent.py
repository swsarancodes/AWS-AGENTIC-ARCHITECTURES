"""Reflexive Metacognitive pattern."""
from patterns.base.agent_base import AgentBase

class ReflexiveMetacognitiveAgent(AgentBase):
    """Monitors and enforces behavioral boundaries."""
    def __init__(self, config):
        super().__init__(config)
        self.boundaries = config.get("boundaries", ["legal", "ethical"])

    def run(self, input_data):
        if self._check_boundaries(input_data):
            return f"Approved: {input_data}"
        return f"Rejected: {input_data} violates boundaries"

    def _check_boundaries(self, data):
        return all(b not in data.lower() for b in ["illegal", "unethical"])

    def get_config(self):
        return self.config
