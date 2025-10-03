"""Graph Memory pattern."""
from patterns.base.agent_base import AgentBase
import networkx as nx

class GraphMemoryAgent(AgentBase):
    """Uses graph structures for relational memory."""
    def __init__(self, config):
        super().__init__(config)
        self.graph = nx.DiGraph()

    def run(self, input_data):
        self.graph.add_node(input_data)
        return f"Added to graph: {input_data}, Total nodes: {len(self.graph.nodes)}"

    def get_config(self):
        return self.config
