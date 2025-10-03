from agent import ReActAgent
from config import REACT_CONFIG

if __name__ == "__main__":
    agent = ReActAgent(REACT_CONFIG)
    query = "Research the latest AI trends"
    result = agent.run(query)
    print("ReAct steps:\n", result)
