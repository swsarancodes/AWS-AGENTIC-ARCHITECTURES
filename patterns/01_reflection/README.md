# Reflection Pattern

The Reflection pattern enables an agent to review and improve its own outputs using AWS Bedrock LLM. This is useful for tasks like code review, quality assurance, and iterative self-improvement.

## Usage

- Configure the agent in `config.py`
- Run the example in `example.py`
- Extend the agent for custom review logic

## Files
- `agent.py`: ReflectionAgent implementation
- `config.py`: Default configuration
- `example.py`: Usage example
- `tests/`: Unit and integration tests

## Configuration Options
- `region`: AWS region for Bedrock
- `model_id`: Bedrock model to use
- `max_iterations`: Number of review cycles
- `temperature`, `top_p`: Model generation parameters
