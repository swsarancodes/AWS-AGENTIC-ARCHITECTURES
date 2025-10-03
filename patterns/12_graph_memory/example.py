from agent import GraphMemoryAgent
from config import GRAPH_MEMORY_CONFIG

if __name__ == "__main__":
    agent = GraphMemoryAgent(GRAPH_MEMORY_CONFIG)
    print(agent.run("Supply chain query"))
