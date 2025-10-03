import unittest
from agent import EpisodicSemanticMemoryAgent
from config import EPISODIC_SEMANTIC_CONFIG

class TestEpisodicSemantic(unittest.TestCase):
    def test_run(self):
        agent = EpisodicSemanticMemoryAgent(EPISODIC_SEMANTIC_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
