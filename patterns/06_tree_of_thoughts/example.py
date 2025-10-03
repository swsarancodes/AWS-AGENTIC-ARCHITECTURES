from agent import TreeOfThoughtsAgent
from config import TOT_CONFIG

if __name__ == "__main__":
    agent = TreeOfThoughtsAgent(TOT_CONFIG)
    print(agent.run("Optimize route"))
