import unittest
from agent import SelfImprovementAgent
from config import SELF_IMPROVEMENT_CONFIG

class TestSelfImprovementIntegration(unittest.TestCase):
    def test_integration(self):
        agent = SelfImprovementAgent(SELF_IMPROVEMENT_CONFIG)
        self.assertIsNotNone(agent.run("moderation"))

if __name__ == "__main__":
    unittest.main()
