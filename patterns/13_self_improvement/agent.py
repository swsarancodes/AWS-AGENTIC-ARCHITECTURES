"""Self-Improvement pattern."""
from patterns.base.agent_base import AgentBase

class SelfImprovementAgent(AgentBase):
    """Iteratively improves performance through feedback."""
    def __init__(self, config):
        super().__init__(config)
        self.performance_history = []

    def run(self, input_data):
        result = self._process(input_data)
        score = self._evaluate(result)
        self.performance_history.append(score)
        return self._improve(result, score)

    def _process(self, data):
        return f"Processed: {data}"

    def _evaluate(self, result):
        return len(result) / 10

    def _improve(self, result, score):
        return f"Improved result (score: {score}): {result}"

    def get_config(self):
        return self.config
