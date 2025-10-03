import unittest
from agent import ReflexiveMetacognitiveAgent
from config import REFLEXIVE_METACOGNITIVE_CONFIG

class TestReflexiveMetacognitiveIntegration(unittest.TestCase):
    def test_integration(self):
        agent = ReflexiveMetacognitiveAgent(REFLEXIVE_METACOGNITIVE_CONFIG)
        self.assertIsNotNone(agent.run("advice"))

if __name__ == "__main__":
    unittest.main()
