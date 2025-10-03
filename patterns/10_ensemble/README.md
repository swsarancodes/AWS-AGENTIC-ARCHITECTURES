# Ensemble Pattern

## Overview

Combines outputs from multiple models to produce more reliable results through voting or averaging.

## Use Cases
- High-stakes decisions
- Reducing bias
- Improving accuracy

## Configuration

```python
config = {
    "models": ["claude-3-opus", "claude-3-sonnet"],
    "aggregation_method": "weighted_vote"
}
```

## Example

```python
from patterns.ensemble.agent import EnsembleAgent
agent = EnsembleAgent(config)
result = agent.run("Critical decision")
```

## Performance

- Accuracy: 10-20% improvement
- Cost: N-models cost
