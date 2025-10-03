# Graph Memory Pattern

## Overview

Stores and queries information as a knowledge graph, enabling relationship-based reasoning.

## Use Cases
- Knowledge management
- Relationship tracking
- Complex queries

## Configuration

```python
config = {
    "graph_db": "neo4j",
    "max_nodes": 10000
}
```

## Example

```python
from patterns.graph_memory.agent import GraphMemoryAgent
agent = GraphMemoryAgent(config)
agent.add_relationship("User", "PREFERS", "DarkMode")
```
