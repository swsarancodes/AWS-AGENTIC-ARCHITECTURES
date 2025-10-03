import unittest
from agent import DryRunHarnessAgent
from config import DRY_RUN_CONFIG

class TestDryRunHarness(unittest.TestCase):
    def test_run(self):
        agent = DryRunHarnessAgent(DRY_RUN_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
