import unittest
from agent import EnsembleAgent
from config import ENSEMBLE_CONFIG

class TestEnsembleIntegration(unittest.TestCase):
    def test_integration(self):
        agent = EnsembleAgent(ENSEMBLE_CONFIG)
        self.assertIsNotNone(agent.run("decision"))

if __name__ == "__main__":
    unittest.main()
