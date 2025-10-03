"""Tree of Thoughts pattern."""
from patterns.base.agent_base import AgentBase
from patterns.base.bedrock_client import BedrockClient

class TreeOfThoughtsAgent(AgentBase):
    """Explores multiple reasoning paths like a tree search."""
    def __init__(self, config):
        super().__init__(config)
        self.bedrock = BedrockClient(region=config.get("region"))
        self.model_id = config.get("model_id", "anthropic.claude-3-sonnet-20240229-v1:0")
        self.depth = config.get("depth", 3)

    def run(self, input_data):
        return self._explore_tree(input_data, 0)

    def _explore_tree(self, node, depth):
        if depth >= self.depth:
            return node
        branches = self._generate_branches(node)
        best = max(branches, key=lambda x: self._evaluate(x))
        return self._explore_tree(best, depth + 1)

    def _generate_branches(self, node):
        return [f"Branch {i} of {node}" for i in range(3)]

    def _evaluate(self, branch):
        return len(branch)

    def get_config(self):
        return self.config
