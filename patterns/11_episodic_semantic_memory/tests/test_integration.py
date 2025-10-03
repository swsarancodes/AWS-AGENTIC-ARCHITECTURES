import unittest
from agent import EpisodicSemanticMemoryAgent
from config import EPISODIC_SEMANTIC_CONFIG

class TestEpisodicSemanticIntegration(unittest.TestCase):
    def test_integration(self):
        agent = EpisodicSemanticMemoryAgent(EPISODIC_SEMANTIC_CONFIG)
        self.assertIsNotNone(agent.run("coaching"))

if __name__ == "__main__":
    unittest.main()
