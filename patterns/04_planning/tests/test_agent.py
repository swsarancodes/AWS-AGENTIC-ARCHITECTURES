import unittest
from agent import PlanningAgent
from config import PLANNING_CONFIG

class TestPlanningAgent(unittest.TestCase):
    def test_run(self):
        agent = PlanningAgent(PLANNING_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
