import unittest
from agent import PEVAgent
from config import PEV_CONFIG

class TestPEVIntegration(unittest.TestCase):
    def test_integration(self):
        agent = PEVAgent(PEV_CONFIG)
        self.assertIsNotNone(agent.run("data"))

if __name__ == "__main__":
    unittest.main()
