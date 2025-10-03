from agent import BlackboardAgent
from config import BLACKBOARD_CONFIG

if __name__ == "__main__":
    agent = BlackboardAgent(BLACKBOARD_CONFIG)
    print(agent.run("Incident response"))
