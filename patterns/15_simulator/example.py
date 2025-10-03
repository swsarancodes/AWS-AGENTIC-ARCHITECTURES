from agent import SimulatorAgent
from config import SIMULATOR_CONFIG

if __name__ == "__main__":
    agent = SimulatorAgent(SIMULATOR_CONFIG)
    print(agent.run("Trading decision"))
