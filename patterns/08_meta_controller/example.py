from agent import MetaControllerAgent
from config import META_CONTROLLER_CONFIG

if __name__ == "__main__":
    agent = MetaControllerAgent(META_CONTROLLER_CONFIG)
    print(agent.run("Fix error"))
