import unittest
from agent import ReflectionAgent
from config import REFLECTION_CONFIG

class TestReflectionIntegration(unittest.TestCase):
    def test_integration(self):
        agent = ReflectionAgent(REFLECTION_CONFIG)
        code = "def add(x, y): return x + y"
        output = agent.run(code)
        self.assertIn("add", output)

if __name__ == "__main__":
    unittest.main()
