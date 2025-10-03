from agent import DryRunHarnessAgent
from config import DRY_RUN_CONFIG

if __name__ == "__main__":
    agent = DryRunHarnessAgent(DRY_RUN_CONFIG)
    print(agent.run("Email campaign"))
