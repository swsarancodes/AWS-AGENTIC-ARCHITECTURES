import unittest
from agent import SimulatorAgent
from config import SIMULATOR_CONFIG

class TestSimulator(unittest.TestCase):
    def test_run(self):
        agent = SimulatorAgent(SIMULATOR_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
