import unittest
from agent import BlackboardAgent
from config import BLACKBOARD_CONFIG

class TestBlackboard(unittest.TestCase):
    def test_run(self):
        agent = BlackboardAgent(BLACKBOARD_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
