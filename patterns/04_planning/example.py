from agent import PlanningAgent
from config import PLANNING_CONFIG

if __name__ == "__main__":
    agent = PlanningAgent(PLANNING_CONFIG)
    print(agent.run("Automate workflow"))
