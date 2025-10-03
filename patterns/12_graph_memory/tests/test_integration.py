import unittest
from agent import GraphMemoryAgent
from config import GRAPH_MEMORY_CONFIG

class TestGraphMemoryIntegration(unittest.TestCase):
    def test_integration(self):
        agent = GraphMemoryAgent(GRAPH_MEMORY_CONFIG)
        self.assertIsNotNone(agent.run("query"))

if __name__ == "__main__":
    unittest.main()
