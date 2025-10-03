from agent import EpisodicSemanticMemoryAgent
from config import EPISODIC_SEMANTIC_CONFIG

if __name__ == "__main__":
    agent = EpisodicSemanticMemoryAgent(EPISODIC_SEMANTIC_CONFIG)
    print(agent.run("Fitness coaching"))
