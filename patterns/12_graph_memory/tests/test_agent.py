import unittest
from agent import GraphMemoryAgent
from config import GRAPH_MEMORY_CONFIG

class TestGraphMemory(unittest.TestCase):
    def test_run(self):
        agent = GraphMemoryAgent(GRAPH_MEMORY_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
