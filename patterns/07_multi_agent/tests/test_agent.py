import unittest
from agent import MultiAgentSystem
from config import MULTI_AGENT_CONFIG

class TestMultiAgentSystem(unittest.TestCase):
    def test_run(self):
        system = MultiAgentSystem(MULTI_AGENT_CONFIG)
        self.assertIsNotNone(system.run("test"))

if __name__ == "__main__":
    unittest.main()
