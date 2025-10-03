import unittest
from agent import ReActAgent
from config import REACT_CONFIG

class TestReActAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ReActAgent(REACT_CONFIG)

    def test_run_returns_list(self):
        result = self.agent.run("test query")
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()
