import unittest
from agent import CellularAutomataAgent
from config import CELLULAR_AUTOMATA_CONFIG

class TestCellularAutomata(unittest.TestCase):
    def test_run(self):
        agent = CellularAutomataAgent(CELLULAR_AUTOMATA_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
