# Tool Using Pattern

The Tool Using pattern enables an agent to integrate external tools (APIs, databases, search engines) with AWS Bedrock LLM to perform complex tasks requiring external data or actions.

## Usage

- Configure tools in `config.py`
- Add custom tools in `tools/` directory
- Run the example in `example.py`

## Files
- `agent.py`: ToolUsingAgent implementation
- `config.py`: Default configuration
- `example.py`: Usage example
- `tools/`: External tool implementations
- `tests/`: Unit and integration tests

## Available Tools
- `currency_tool.py`: Currency conversion
- `web_search_tool.py`: Web search using Bedrock Knowledge Bases

## Configuration Options
- `region`: AWS region for Bedrock
- `model_id`: Bedrock model to use
- `tools_enabled`: List of enabled tools
- `tool_timeout`: Timeout for tool execution
