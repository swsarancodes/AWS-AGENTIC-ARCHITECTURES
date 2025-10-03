import unittest
from agent import SelfImprovementAgent
from config import SELF_IMPROVEMENT_CONFIG

class TestSelfImprovement(unittest.TestCase):
    def test_run(self):
        agent = SelfImprovementAgent(SELF_IMPROVEMENT_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
