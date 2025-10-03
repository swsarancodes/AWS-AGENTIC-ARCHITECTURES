# Tree of Thoughts Pattern

## Overview

Tree of Thoughts explores multiple reasoning paths simultaneously, evaluating and pruning branches to find optimal solutions.

## Use Cases
- Creative writing
- Complex problem solving
- Strategic planning
- Game playing

## Configuration

```python
config = {
    "max_branches": 5,
    "max_depth": 4,
    "evaluation_threshold": 0.7
}
```

## Example

```python
from patterns.tree_of_thoughts.agent import TreeOfThoughtsAgent
agent = TreeOfThoughtsAgent(config)
result = agent.run("Design innovative solution")
```

## Performance

- Quality: Higher than linear reasoning
- Cost: 3-5x single path
