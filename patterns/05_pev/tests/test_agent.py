import unittest
from agent import PEVAgent
from config import PEV_CONFIG

class TestPEVAgent(unittest.TestCase):
    def test_run(self):
        agent = PEVAgent(PEV_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
