import unittest
from agent import ReflectionAgent
from config import REFLECTION_CONFIG

class TestReflectionAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ReflectionAgent(REFLECTION_CONFIG)

    def test_run_returns_string(self):
        result = self.agent.run("def foo(): pass")
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
