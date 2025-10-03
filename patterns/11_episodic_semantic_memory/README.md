# Episodic & Semantic Memory Pattern

## Overview

Implements episodic (events) and semantic (knowledge) memory for long-term context retention.

## Use Cases
- Conversational agents
- Personalization
- Learning systems

## Configuration

```python
config = {
    "episodic_db": "postgresql",
    "semantic_db": "chromadb"
}
```

## Example

```python
from patterns.episodic_semantic_memory.agent import MemoryAgent
agent = MemoryAgent(config)
agent.store_episode("User prefers dark mode")
result = agent.run("What are my preferences?")
```

## Performance

- Storage: Less than 50ms per item
- Retrieval: Less than 200ms
