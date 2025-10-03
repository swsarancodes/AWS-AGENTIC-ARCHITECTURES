import unittest
from agent import ToolUsingAgent
from config import TOOL_USING_CONFIG

class TestToolUsingIntegration(unittest.TestCase):
    def test_integration(self):
        agent = ToolUsingAgent(TOOL_USING_CONFIG)
        query = "Currency conversion"
        output = agent.run(query)
        self.assertIsNotNone(output)

if __name__ == "__main__":
    unittest.main()
