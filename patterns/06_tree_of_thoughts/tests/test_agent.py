import unittest
from agent import TreeOfThoughtsAgent
from config import TOT_CONFIG

class TestTreeOfThoughtsAgent(unittest.TestCase):
    def test_run(self):
        agent = TreeOfThoughtsAgent(TOT_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
