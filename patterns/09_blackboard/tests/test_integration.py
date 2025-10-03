import unittest
from agent import BlackboardAgent
from config import BLACKBOARD_CONFIG

class TestBlackboardIntegration(unittest.TestCase):
    def test_integration(self):
        agent = BlackboardAgent(BLACKBOARD_CONFIG)
        self.assertIsNotNone(agent.run("incident"))

if __name__ == "__main__":
    unittest.main()
