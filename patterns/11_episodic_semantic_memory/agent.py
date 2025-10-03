"""Episodic+Semantic Memory pattern."""
from patterns.base.agent_base import AgentBase
from patterns.base.memory_base import MemoryBase

class EpisodicSemanticMemoryAgent(AgentBase):
    """Combines episodic and semantic memory for personalization."""
    def __init__(self, config):
        super().__init__(config)
        self.episodic_memory = []  # Recent events
        self.semantic_memory = {}  # General knowledge

    def run(self, input_data):
        self.episodic_memory.append(input_data)
        context = self._retrieve_context(input_data)
        return f"Response with context: {context}"

    def _retrieve_context(self, query):
        return {"episodic": self.episodic_memory[-3:], "semantic": self.semantic_memory}

    def get_config(self):
        return self.config
