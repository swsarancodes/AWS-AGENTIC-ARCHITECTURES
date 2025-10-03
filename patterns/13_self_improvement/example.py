from agent import SelfImprovementAgent
from config import SELF_IMPROVEMENT_CONFIG

if __name__ == "__main__":
    agent = SelfImprovementAgent(SELF_IMPROVEMENT_CONFIG)
    print(agent.run("Content moderation"))
