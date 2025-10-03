import unittest
from agent import MultiAgentSystem
from config import MULTI_AGENT_CONFIG

class TestMultiAgentIntegration(unittest.TestCase):
    def test_integration(self):
        system = MultiAgentSystem(MULTI_AGENT_CONFIG)
        self.assertIsNotNone(system.run("analysis"))

if __name__ == "__main__":
    unittest.main()
