# Dry-Run Harness Pattern

## Overview

Executes agent actions in simulation mode before real execution, enabling risk-free testing.

## Use Cases
- Risk mitigation
- Testing workflows
- Cost estimation

## Configuration

```python
config = {
    "dry_run_mode": True,
    "log_actions": True
}
```

## Example

```python
from patterns.dry_run_harness.agent import DryRunAgent
agent = DryRunAgent(config)
result = agent.run("Delete customer records")
```
