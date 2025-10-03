from agent import ReflexiveMetacognitiveAgent
from config import REFLEXIVE_METACOGNITIVE_CONFIG

if __name__ == "__main__":
    agent = ReflexiveMetacognitiveAgent(REFLEXIVE_METACOGNITIVE_CONFIG)
    print(agent.run("Legal advice"))
