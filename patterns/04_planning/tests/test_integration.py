import unittest
from agent import PlanningAgent
from config import PLANNING_CONFIG

class TestPlanningIntegration(unittest.TestCase):
    def test_integration(self):
        agent = PlanningAgent(PLANNING_CONFIG)
        self.assertIsNotNone(agent.run("workflow"))

if __name__ == "__main__":
    unittest.main()
