import unittest
from agent import EnsembleAgent
from config import ENSEMBLE_CONFIG

class TestEnsemble(unittest.TestCase):
    def test_run(self):
        agent = EnsembleAgent(ENSEMBLE_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
