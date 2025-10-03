import unittest
from agent import ReActAgent
from config import REACT_CONFIG

class TestReActIntegration(unittest.TestCase):
    def test_integration(self):
        agent = ReActAgent(REACT_CONFIG)
        query = "Find information"
        output = agent.run(query)
        self.assertGreater(len(output), 0)

if __name__ == "__main__":
    unittest.main()
