import unittest
from agent import TreeOfThoughtsAgent
from config import TOT_CONFIG

class TestTreeOfThoughtsIntegration(unittest.TestCase):
    def test_integration(self):
        agent = TreeOfThoughtsAgent(TOT_CONFIG)
        self.assertIsNotNone(agent.run("route"))

if __name__ == "__main__":
    unittest.main()
