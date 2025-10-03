"""Dry-Run Harness pattern."""
from patterns.base.agent_base import AgentBase

class DryRunHarnessAgent(AgentBase):
    """Tests actions in safe mode before real execution."""
    def __init__(self, config):
        super().__init__(config)
        self.dry_run = config.get("dry_run", True)

    def run(self, input_data):
        if self.dry_run:
            return f"DRY RUN: Would execute {input_data}"
        return f"EXECUTED: {input_data}"

    def get_config(self):
        return self.config
