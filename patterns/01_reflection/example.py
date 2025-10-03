
from agent import ReflectionAgent
from config import REFLECTION_CONFIG

if __name__ == "__main__":
    agent = ReflectionAgent(REFLECTION_CONFIG)
    code_sample = "def add(x, y):\n    return x + y"
    improved_code = agent.run(code_sample)
    print("Improved code:\n", improved_code)
