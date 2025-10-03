from agent import CellularAutomataAgent
from config import CELLULAR_AUTOMATA_CONFIG

if __name__ == "__main__":
    agent = CellularAutomataAgent(CELLULAR_AUTOMATA_CONFIG)
    print(agent.run("Warehouse robotics"))
