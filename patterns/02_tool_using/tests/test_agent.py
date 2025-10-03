import unittest
from agent import ToolUsingAgent
from config import TOOL_USING_CONFIG

class TestToolUsingAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ToolUsingAgent(TOOL_USING_CONFIG)

    def test_agent_has_tools(self):
        self.assertIn("currency", self.agent.tools)
        self.assertIn("web_search", self.agent.tools)

if __name__ == "__main__":
    unittest.main()
