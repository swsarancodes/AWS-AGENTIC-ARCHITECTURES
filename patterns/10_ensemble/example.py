from agent import EnsembleAgent
from config import ENSEMBLE_CONFIG

if __name__ == "__main__":
    agent = EnsembleAgent(ENSEMBLE_CONFIG)
    print(agent.run("Investment decision"))
