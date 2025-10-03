import unittest
from agent import MetaControllerAgent
from config import META_CONTROLLER_CONFIG

class TestMetaController(unittest.TestCase):
    def test_run(self):
        agent = MetaControllerAgent(META_CONTROLLER_CONFIG)
        self.assertIsNotNone(agent.run("test"))

if __name__ == "__main__":
    unittest.main()
