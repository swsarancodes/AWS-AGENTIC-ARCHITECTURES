import unittest
from agent import CellularAutomataAgent
from config import CELLULAR_AUTOMATA_CONFIG

class TestCellularAutomataIntegration(unittest.TestCase):
    def test_integration(self):
        agent = CellularAutomataAgent(CELLULAR_AUTOMATA_CONFIG)
        self.assertIsNotNone(agent.run("robotics"))

if __name__ == "__main__":
    unittest.main()
