import unittest
from agent import DryRunHarnessAgent
from config import DRY_RUN_CONFIG

class TestDryRunHarnessIntegration(unittest.TestCase):
    def test_integration(self):
        agent = DryRunHarnessAgent(DRY_RUN_CONFIG)
        self.assertIsNotNone(agent.run("email"))

if __name__ == "__main__":
    unittest.main()
