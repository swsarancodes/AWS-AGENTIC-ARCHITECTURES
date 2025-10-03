from agent import MultiAgentSystem
from config import MULTI_AGENT_CONFIG

if __name__ == "__main__":
    system = MultiAgentSystem(MULTI_AGENT_CONFIG)
    print(system.run("Market analysis"))
