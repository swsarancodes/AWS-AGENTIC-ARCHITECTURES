import unittest
from agent import SimulatorAgent
from config import SIMULATOR_CONFIG

class TestSimulatorIntegration(unittest.TestCase):
    def test_integration(self):
        agent = SimulatorAgent(SIMULATOR_CONFIG)
        self.assertIsNotNone(agent.run("trading"))

if __name__ == "__main__":
    unittest.main()
