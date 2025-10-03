import unittest
from agent import ReflexiveMetacognitiveAgent
from config import REFLEXIVE_METACOGNITIVE_CONFIG

class TestReflexiveMetacognitive(unittest.TestCase):
    def test_run(self):
        agent = ReflexiveMetacognitiveAgent(REFLEXIVE_METACOGNITIVE_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
