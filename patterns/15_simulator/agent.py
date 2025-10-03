"""Simulator pattern."""
from patterns.base.agent_base import AgentBase

class SimulatorAgent(AgentBase):
    """Simulates actions to assess risk before execution."""
    def __init__(self, config):
        super().__init__(config)
        self.simulation_depth = config.get("simulation_depth", 10)

    def run(self, input_data):
        simulations = self._run_simulations(input_data)
        best = self._select_best(simulations)
        return f"Best action: {best}"

    def _run_simulations(self, data):
        return [f"Sim {i}: {data}" for i in range(self.simulation_depth)]

    def _select_best(self, simulations):
        return max(simulations, key=len)

    def get_config(self):
        return self.config
