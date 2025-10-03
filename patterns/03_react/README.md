# ReAct Pattern

The ReAct (Reasoning and Acting) pattern enables an agent to interleave reasoning and action steps to solve complex tasks requiring multi-step problem-solving.

## Usage

- Configure the agent in `config.py`
- Run the example in `example.py`
- Customize reasoning and action logic

## Files
- `agent.py`: ReActAgent implementation
- `config.py`: Default configuration
- `example.py`: Usage example
- `tests/`: Unit and integration tests

## Configuration Options
- `region`: AWS region for Bedrock
- `model_id`: Bedrock model to use
- `max_steps`: Maximum reasoning/action steps
- `temperature`, `top_p`: Model generation parameters
