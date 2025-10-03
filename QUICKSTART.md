# Quick Start Guide

Get up and running with AWS Agentic Architectures in 5 minutes!

## Prerequisites
- Python 3.10 or higher
- AWS Account with Bedrock access
- AWS CLI configured

## Installation

### 1. Clone and Navigate
```powershell
cd "c:\Users\GANES\OneDrive\Documents\REACT\AGENT PATTERNS\AWS-AGENTIC-ARCHITECTURES"
```

### 2. Install Dependencies
```powershell
# Using pip
pip install -r requirements.txt

# Or using UV (recommended)
pip install uv
uv pip install -r requirements.txt
```

### 3. Configure Environment
```powershell
# Copy example env file
Copy-Item .env.example .env

# Edit .env with your AWS credentials
notepad .env
```

Required environment variables:
```
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0
```

## Quick Examples

### Example 1: Simple Reflection Pattern
```python
from patterns.reflection.agent import ReflectionAgent

agent = ReflectionAgent()
result = agent.run("Explain quantum computing in simple terms")
print(result)
```

### Example 2: ReAct Pattern with Tools
```python
from patterns.react.agent import ReActAgent

agent = ReActAgent()
result = agent.run("What is the weather like today?")
print(result)
```

### Example 3: Multi-Agent System
```python
from patterns.multi_agent.agent import MultiAgentSystem

system = MultiAgentSystem()
result = system.run("Analyze market trends and generate report")
print(result)
```

## Running the API

### Start the FastAPI Server
```powershell
uvicorn api.main:app --reload
```

Access the API at: http://localhost:8000

### API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Example API Request
```powershell
# Using curl
curl -X POST "http://localhost:8000/patterns/reflection/run" `
  -H "Content-Type: application/json" `
  -H "X-API-Key: your-api-key" `
  -d '{\"input\": \"Explain AI\", \"config\": {}}'
```

## Using Docker

### Build and Run with Docker Compose
```powershell
docker-compose up -d
```

This starts:
- API server (port 8000)
- PostgreSQL database
- Redis cache
- ChromaDB vector store
- Prometheus monitoring
- Grafana dashboards

### Access Services
- API: http://localhost:8000
- Grafana: http://localhost:3000 (admin/admin)
- Prometheus: http://localhost:9090

## Testing Patterns

### Run All Tests
```powershell
pytest tests/ -v
```

### Run Specific Pattern Tests
```powershell
pytest tests/unit/patterns/test_reflection.py -v
```

### Run Benchmarks
```powershell
python -m evaluation.benchmarks.performance_tests
```

## Interactive Examples

### Jupyter Notebooks
```powershell
jupyter notebook examples/notebooks/
```

Open `getting_started.ipynb` for an interactive tutorial.

### Streamlit Demo
```powershell
streamlit run examples/demos/streamlit_app.py
```

### CLI Demo
```powershell
python examples/demos/cli_demo.py --pattern reflection --prompt "Hello world"
```

## Common Use Cases

### 1. Customer Support Bot
```python
from examples.use_cases.customer_support.agent import CustomerSupportAgent

agent = CustomerSupportAgent()
response = agent.run("How do I reset my password?")
```

### 2. Code Generation
```python
from examples.use_cases.code_generation.agent import CodeGenerationAgent

agent = CodeGenerationAgent()
code = agent.run("Create a Python function to sort a list")
```

### 3. Research Assistant
```python
from examples.use_cases.research_assistant.agent import ResearchAssistant

agent = ResearchAssistant()
report = agent.run("Summarize latest AI trends")
```

## Monitoring

### View Metrics
```powershell
# Open Prometheus
start http://localhost:9090

# Open Grafana
start http://localhost:3000
```

### Check Logs
```powershell
# API logs
docker-compose logs -f api

# All services
docker-compose logs -f
```

## Troubleshooting

### AWS Credentials Issue
```powershell
aws configure
aws bedrock list-foundation-models --region us-east-1
```

### Import Errors
```powershell
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Port Already in Use
```powershell
# Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

## Next Steps

1. **Explore Patterns**: Check `patterns/` for all 17 implementations
2. **Read Documentation**: See `docs/GETTING_STARTED.md` for detailed guide
3. **Deploy to AWS**: Follow `docs/DEPLOYMENT.md`
4. **Customize**: Modify patterns in `patterns/` directories
5. **Contribute**: Check GitHub for contribution guidelines

## Pattern Cheat Sheet

| Pattern | Use Case | File |
|---------|----------|------|
| Reflection | Self-evaluation & improvement | `patterns/01_reflection/` |
| Tool Using | External tool integration | `patterns/02_tool_using/` |
| ReAct | Reasoning + Acting | `patterns/03_react/` |
| Planning | Multi-step task planning | `patterns/04_planning/` |
| PEV | Plan-Execute-Verify | `patterns/05_pev/` |
| Tree of Thoughts | Explore multiple solutions | `patterns/06_tree_of_thoughts/` |
| Multi-Agent | Collaborative agents | `patterns/07_multi_agent/` |
| Meta Controller | Agent orchestration | `patterns/08_meta_controller/` |
| Blackboard | Shared knowledge space | `patterns/09_blackboard/` |
| Ensemble | Combine multiple models | `patterns/10_ensemble/` |
| Memory | Long-term context | `patterns/11_episodic_semantic_memory/` |
| Graph Memory | Knowledge graphs | `patterns/12_graph_memory/` |
| Self-Improvement | Continuous learning | `patterns/13_self_improvement/` |
| Dry-Run | Preview actions | `patterns/14_dry_run_harness/` |
| Simulator | Environment simulation | `patterns/15_simulator/` |
| Metacognitive | Self-awareness | `patterns/16_reflexive_metacognitive/` |
| Cellular Automata | Emergent behavior | `patterns/17_cellular_automata/` |

## Support

- Documentation: `docs/`
- Issues: Check GitHub Issues
- Examples: `examples/`
- API Reference: `docs/API_REFERENCE.md`

Happy coding! 🚀
