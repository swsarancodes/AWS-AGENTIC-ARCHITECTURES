# Meta-Controller Pattern

## Overview

A meta-controller dynamically routes tasks to specialized sub-agents based on task requirements.

## Use Cases
- Dynamic workflow routing
- Specialized task distribution
- Load balancing
- Intelligent orchestration

## Configuration

```python
config = {
    "available_agents": ["reflection", "tool_using"],
    "selection_strategy": "best_fit"
}
```

## Example

```python
from patterns.meta_controller.agent import MetaControllerAgent
agent = MetaControllerAgent(config)
result = agent.run("Complex task")
```

## Performance

- Routing overhead: <1 second
- Flexibility: High
