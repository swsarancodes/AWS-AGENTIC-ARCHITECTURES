# Reflexive Metacognitive Pattern

## Overview

Agent monitors its own thinking process and adjusts reasoning strategies dynamically.

## Use Cases
- Self-aware reasoning
- Strategy adaptation
- Confidence estimation

## Configuration

```python
config = {
    "monitoring_depth": 3,
    "confidence_threshold": 0.8
}
```

## Example

```python
from patterns.reflexive_metacognitive.agent import MetacognitiveAgent
agent = MetacognitiveAgent(config)
result = agent.run("Complex reasoning task")
```
