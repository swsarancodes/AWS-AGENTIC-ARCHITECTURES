from agent import PEVAgent
from config import PEV_CONFIG

if __name__ == "__main__":
    agent = PEVAgent(PEV_CONFIG)
    print(agent.run("Extract data"))
