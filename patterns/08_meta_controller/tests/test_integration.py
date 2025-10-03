import unittest
from agent import MetaControllerAgent
from config import META_CONTROLLER_CONFIG

class TestMetaControllerIntegration(unittest.TestCase):
    def test_integration(self):
        agent = MetaControllerAgent(META_CONTROLLER_CONFIG)
        self.assertIsNotNone(agent.run("helpdesk"))

if __name__ == "__main__":
    unittest.main()
