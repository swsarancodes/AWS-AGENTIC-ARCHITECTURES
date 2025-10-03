"""Blackboard pattern."""
from patterns.base.agent_base import AgentBase

class BlackboardAgent(AgentBase):
    """Shared knowledge space for dynamic collaboration."""
    def __init__(self, config):
        super().__init__(config)
        self.blackboard = {}

    def run(self, input_data):
        self.blackboard["input"] = input_data
        self._process()
        return self.blackboard

    def _process(self):
        self.blackboard["processed"] = True

    def get_config(self):
        return self.config
