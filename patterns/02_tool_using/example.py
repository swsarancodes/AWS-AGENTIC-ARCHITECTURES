from agent import ToolUsingAgent
from config import TOOL_USING_CONFIG

if __name__ == "__main__":
    agent = ToolUsingAgent(TOOL_USING_CONFIG)
    query = "What is the current exchange rate for USD to EUR?"
    result = agent.run(query)
    print("Result:\n", result)
