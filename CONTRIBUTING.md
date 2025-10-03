# Contributing to AWS Agentic Architectures

Thank you for your interest in contributing! This document provides guidelines and instructions.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Collaborate openly

## How to Contribute

### Reporting Bugs

1. Check existing issues first
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, AWS region)
   - Error messages and logs

### Suggesting Enhancements

1. Open an issue with "Enhancement" label
2. Describe the feature and use case
3. Explain why it would be useful
4. Provide examples if possible

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write/update tests
5. Update documentation
6. Commit with clear messages
7. Push to your fork
8. Open a Pull Request

## Development Setup

### Prerequisites
```powershell
# Python 3.10+
python --version

# UV (recommended)
pip install uv

# Git
git --version
```

### Clone and Setup
```powershell
git clone https://github.com/yourusername/aws-agentic-architectures.git
cd aws-agentic-architectures

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install pytest black flake8 mypy
```

### Environment Configuration
```powershell
Copy-Item .env.example .env
# Edit .env with your AWS credentials
```

## Coding Standards

### Python Style Guide

Follow PEP 8 with these specifics:

```python
# Use type hints
def process_data(input_text: str, max_length: int = 100) -> dict:
    """
    Process input text and return results.
    
    Args:
        input_text: The text to process
        max_length: Maximum length of output
        
    Returns:
        Dictionary containing processed results
    """
    pass

# Use descriptive names
class ReflectionAgent(AgentBase):
    def __init__(self, config: dict):
        super().__init__(config)
```

### Code Formatting

```powershell
# Format code with black
black patterns/ api/ utils/

# Check style with flake8
flake8 patterns/ api/ utils/

# Type checking with mypy
mypy patterns/ api/ utils/
```

### Import Organization

```python
# Standard library
import json
import logging
from typing import List, Dict, Optional

# Third-party
import boto3
from fastapi import FastAPI
from pydantic import BaseModel

# Local
from patterns.base.agent_base import AgentBase
from utils.config_loader import ConfigLoader
```

## Project Structure

### Adding a New Pattern

1. Create directory: `patterns/18_new_pattern/`
2. Add required files:
   ```
   patterns/18_new_pattern/
   ├── __init__.py
   ├── agent.py          # Main implementation
   ├── config.py         # Configuration
   ├── example.py        # Usage example
   ├── README.md         # Documentation
   └── tests/
       ├── __init__.py
       ├── test_agent.py
       └── test_integration.py
   ```

3. Implement AgentBase:
```python
from patterns.base.agent_base import AgentBase

class NewPatternAgent(AgentBase):
    def run(self, input_data: str) -> dict:
        """Execute the pattern logic."""
        # Implementation
        pass
```

4. Add configuration:
```python
NEW_PATTERN_CONFIG = {
    "region": "us-east-1",
    "model_id": "anthropic.claude-3-sonnet-20240229-v1:0",
    "pattern_specific_param": "value"
}
```

5. Write tests:
```python
import unittest
from patterns.new_pattern.agent import NewPatternAgent

class TestNewPatternAgent(unittest.TestCase):
    def test_run(self):
        agent = NewPatternAgent()
        result = agent.run("test input")
        self.assertIsNotNone(result)
```

### Adding an API Endpoint

1. Create router in `api/routers/`:
```python
from fastapi import APIRouter

router = APIRouter(prefix="/new", tags=["new"])

@router.get("/endpoint")
def new_endpoint():
    return {"message": "success"}
```

2. Register in `api/main.py`:
```python
from api.routers import new_router
app.include_router(new_router.router)
```

## Testing

### Running Tests

```powershell
# All tests
pytest tests/ -v

# Specific test file
pytest tests/unit/patterns/test_reflection.py -v

# With coverage
pytest tests/ --cov=patterns --cov=api --cov-report=html
```

### Writing Tests

```python
# Unit test example
import unittest
from patterns.reflection.agent import ReflectionAgent

class TestReflectionAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ReflectionAgent()
    
    def test_run_returns_dict(self):
        result = self.agent.run("test")
        self.assertIsInstance(result, dict)
    
    def tearDown(self):
        pass

# Integration test example
import pytest
from api.main import app
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
```

## Documentation

### Docstring Format

```python
def function_name(param1: str, param2: int = 10) -> dict:
    """
    Short description.
    
    Longer description with more details about what the function does,
    its behavior, and any important notes.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter (default: 10)
        
    Returns:
        Dictionary containing:
            - key1: Description
            - key2: Description
            
    Raises:
        ValueError: When param1 is empty
        RuntimeError: When AWS connection fails
        
    Example:
        >>> result = function_name("test", 20)
        >>> print(result)
        {'key1': 'value1', 'key2': 'value2'}
    """
    pass
```

### README Template

```markdown
# Pattern Name

Brief description of what this pattern does.

## How It Works

Explain the mechanism and flow.

## Use Cases

- Use case 1
- Use case 2
- Use case 3

## Configuration

\`\`\`python
config = {
    "param1": "value1",
    "param2": 100
}
\`\`\`

## Example

\`\`\`python
from patterns.pattern_name.agent import PatternAgent

agent = PatternAgent()
result = agent.run("input")
\`\`\`

## References

- Link to paper
- Link to documentation
```

## Version Control

### Commit Messages

Follow conventional commits:

```
type(scope): subject

body

footer
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance

Examples:
```
feat(patterns): add quantum reasoning pattern

Implements quantum-inspired reasoning for complex problem solving.
Includes unit tests and integration tests.

Closes #123
```

```
fix(api): resolve authentication middleware issue

Authentication was failing for valid API keys due to
header parsing error.

Fixes #456
```

### Branch Naming

- Feature: `feature/pattern-name`
- Bug fix: `fix/issue-description`
- Documentation: `docs/update-readme`
- Refactor: `refactor/improve-bedrock-client`

## Review Process

### Pull Request Checklist

- [ ] Code follows style guidelines
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Commit messages are clear
- [ ] Changes are focused and minimal

### Code Review Guidelines

Reviewers should check:
1. Code quality and style
2. Test coverage
3. Documentation clarity
4. Performance implications
5. Security considerations
6. AWS best practices

## Release Process

1. Update CHANGELOG.md
2. Bump version in pyproject.toml
3. Create release branch
4. Run full test suite
5. Create GitHub release
6. Tag version (`git tag v1.0.0`)
7. Deploy to production

## Questions?

- Open an issue with "Question" label
- Check existing documentation
- Review examples in `examples/`

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🙌
