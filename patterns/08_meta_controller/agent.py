"""Meta-Controller pattern."""
from patterns.base.agent_base import AgentBase

class MetaControllerAgent(AgentBase):
    """Routes tasks to specialized sub-agents."""
    def __init__(self, config):
        super().__init__(config)
        self.sub_agents = {"technical": "TechAgent", "billing": "BillingAgent"}

    def run(self, input_data):
        agent_type = self._route(input_data)
        return f"Routed to {agent_type}: {input_data}"

    def _route(self, input_data):
        return "technical" if "error" in input_data.lower() else "billing"

    def get_config(self):
        return self.config
