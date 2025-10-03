# AWS Agentic Architectures

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-orange.svg)](https://aws.amazon.com/bedrock/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-ready framework implementing 17 advanced agentic patterns powered by AWS Bedrock and Claude 3.

---

## Table of Contents

- [Features](#features)
- [Patterns Overview](#patterns-overview)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [API Documentation](#api-documentation)
- [Docker Deployment](#docker-deployment)
- [AWS Deployment](#aws-deployment)
- [Security](#security)
- [Monitoring & Evaluation](#monitoring--evaluation)
- [Testing](#testing)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### 17 Production-Ready Agentic Patterns
See detailed documentation in each pattern folder:

- [01 - Reflection](patterns/01_reflection/README.md): Self-evaluating agents with iterative improvement
- [02 - Tool Using](patterns/02_tool_using/README.md): External API and tool integration
- [03 - ReAct](patterns/03_react/README.md): Reasoning and acting with thought-action cycles
- [04 - Planning](patterns/04_planning/README.md): Multi-step task decomposition
- [05 - PEV](patterns/05_pev/README.md): Plan-Execute-Verify validation loops
- [06 - Tree of Thoughts](patterns/06_tree_of_thoughts/README.md): Parallel solution exploration
- [07 - Multi-Agent](patterns/07_multi_agent/README.md): Collaborative agent coordination
- [08 - Meta-Controller](patterns/08_meta_controller/README.md): Dynamic routing and orchestration
- [09 - Blackboard](patterns/09_blackboard/README.md): Shared knowledge architecture
- [10 - Ensemble](patterns/10_ensemble/README.md): Model combination and consensus
- [11 - Memory Systems](patterns/11_episodic_semantic_memory/README.md): Episodic and semantic memory
- [12 - Graph Memory](patterns/12_graph_memory/README.md): Knowledge graph relationships
- [13 - Self-Improvement](patterns/13_self_improvement/README.md): Adaptive learning
- [14 - Dry-Run Harness](patterns/14_dry_run_harness/README.md): Risk-free action preview
- [15 - Simulator](patterns/15_simulator/README.md): Environment modeling
- [16 - Metacognitive](patterns/16_reflexive_metacognitive/README.md): Self-aware cognitive monitoring
- [17 - Cellular Automata](patterns/17_cellular_automata/README.md): Emergent behavior patterns

### Enterprise-Grade Infrastructure
- AWS Bedrock Integration with Claude 3 Sonnet
- FastAPI REST API with authentication & rate limiting
- Docker & Kubernetes deployment ready
- Multi-database Support: PostgreSQL, Redis, ChromaDB
- Infrastructure as Code: Terraform, CloudFormation, CDK
- Prometheus & Grafana monitoring stack
- Structured Logging with audit trails
- Comprehensive Testing: Unit, Integration, E2E
- CI/CD Ready with GitHub Actions support

### Security & Compliance
- API Key authentication
- Role-based access control (RBAC)
- Encryption at rest and in transit
- Audit logging for compliance
- AWS IAM integration
- Secrets management

### Evaluation Framework
- Performance benchmarking
- Accuracy testing
- Cost analysis (per pattern)
- Quality metrics (precision, recall, F1)
- Reliability metrics (uptime, error rate)
- Efficiency metrics (throughput, latency)

---

## Patterns Overview

| # | Pattern | Use Case | Complexity |
|---|---------|----------|------------|
| 01 | [Reflection](patterns/01_reflection/README.md) | Self-improving essay writing | Medium |
| 02 | [Tool Using](patterns/02_tool_using/README.md) | Web search, API calls | Low |
| 03 | [ReAct](patterns/03_react/README.md) | Complex Q&A with reasoning | Medium |
| 04 | [Planning](patterns/04_planning/README.md) | Multi-step task execution | Medium |
| 05 | [PEV](patterns/05_pev/README.md) | Validated task completion | High |
| 06 | [Tree of Thoughts](patterns/06_tree_of_thoughts/README.md) | Creative problem solving | High |
| 07 | [Multi-Agent](patterns/07_multi_agent/README.md) | Team collaboration | High |
| 08 | [Meta-Controller](patterns/08_meta_controller/README.md) | Dynamic agent routing | Medium |
| 09 | [Blackboard](patterns/09_blackboard/README.md) | Shared knowledge systems | High |
| 10 | [Ensemble](patterns/10_ensemble/README.md) | Model consensus | Medium |
| 11 | [Memory](patterns/11_episodic_semantic_memory/README.md) | Long-term context | Medium |
| 12 | [Graph Memory](patterns/12_graph_memory/README.md) | Relationship tracking | High |
| 13 | [Self-Improvement](patterns/13_self_improvement/README.md) | Continuous learning | High |
| 14 | [Dry-Run](patterns/14_dry_run_harness/README.md) | Risk mitigation | Low |
| 15 | [Simulator](patterns/15_simulator/README.md) | Scenario testing | High |
| 16 | [Metacognitive](patterns/16_reflexive_metacognitive/README.md) | Self-awareness | High |
| 17 | [Cellular Automata](patterns/17_cellular_automata/README.md) | Emergent patterns | High |

---

## Quick Start

### Prerequisites
```bash
# Required
- Python 3.10+
- AWS Account with Bedrock access
- Docker & Docker Compose (optional)
- Git

# Optional
- Kubernetes cluster
- Terraform CLI
```

### 5-Minute Setup

```powershell
# 1. Clone the repository
git clone https://github.com/swsarancodes/AWS-AGENTIC-ARCHITECTURES.git
cd AWS-AGENTIC-ARCHITECTURES

# 2. Set up environment
Copy-Item .env.example .env
# Edit .env with your AWS credentials

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the API
uvicorn api.main:app --reload

# 5. Open your browser
start http://localhost:8000/docs
```

### Docker Quick Start

```powershell
# Start all services
docker-compose up -d

# Access services
# API: http://localhost:8000
# Grafana: http://localhost:3000
# Prometheus: http://localhost:9090
```

---


## Installation

### Standard Installation

```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Alternatively, use UV for faster installs
pip install uv
uv pip install -r requirements.txt
```

### Development Installation

```powershell
# Install with development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/ -v
```

---


## API Documentation

### Start the API Server

```powershell
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

### Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Core Endpoints

#### Health Check
```http
GET /health
```

#### List All Patterns
```http
GET /patterns
```

#### Execute Pattern
```http
POST /patterns/{pattern_name}/run
Content-Type: application/json
X-API-Key: your-api-key-here

{
  "input": "Your task description",
  "config": {
    "max_iterations": 3,
    "temperature": 0.7
  }
}
```

#### Get Pattern Details
```http
GET /patterns/{pattern_name}
```

### Example cURL Request

```bash
curl -X POST "http://localhost:8000/patterns/reflection/run" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "input": "Explain quantum computing",
    "config": {"max_iterations": 2}
  }'
```

---

## Docker Deployment

### Using Docker Compose (Recommended)

```powershell
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down

# Rebuild and restart
docker-compose up --build -d
```

### Services Included

- **API**: FastAPI application (port 8000)
- **PostgreSQL**: Primary database (port 5432)
- **Redis**: Cache layer (port 6379)
- **ChromaDB**: Vector store (port 8001)
- **Prometheus**: Metrics collection (port 9090)
- **Grafana**: Visualization (port 3000)
- **Nginx**: Reverse proxy (port 80)

### Standalone Docker

```powershell
# Build image
docker build -t agentic-patterns:latest .

# Run container
docker run -d \
  -p 8000:8000 \
  -e AWS_REGION=us-east-1 \
  -e BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0 \
  --name agentic-api \
  agentic-patterns:latest
```

---

## AWS Deployment

### CloudFormation

```powershell
cd infrastructure/aws/cloudformation

# Deploy Bedrock setup
aws cloudformation create-stack \
  --stack-name agentic-bedrock \
  --template-body file://bedrock-setup.yaml \
  --capabilities CAPABILITY_IAM

# Deploy Lambda functions
aws cloudformation create-stack \
  --stack-name agentic-lambda \
  --template-body file://lambda-functions.yaml \
  --capabilities CAPABILITY_IAM
```

### Terraform

```powershell
cd infrastructure/aws/terraform

# Initialize
terraform init

# Plan deployment
terraform plan -out=tfplan

# Apply
terraform apply tfplan
```

### AWS CDK

```powershell
cd infrastructure/aws/cdk

# Install dependencies
pip install -r requirements.txt

# Deploy
cdk deploy
```

### Kubernetes

```powershell
# Apply manifests
kubectl apply -f infrastructure/kubernetes/namespace.yaml
kubectl apply -f infrastructure/kubernetes/deployment.yaml
kubectl apply -f infrastructure/kubernetes/service.yaml
kubectl apply -f infrastructure/kubernetes/ingress.yaml

# Check status
kubectl get pods -n agentic-architectures
```

---

## Security

### Authentication

```python
# API Key authentication (default)
headers = {
    "X-API-Key": "your-secure-api-key",
    "Content-Type": "application/json"
}
```

### Role-Based Access Control

```python
from security.access_control import AccessControl

ac = AccessControl()
ac.check_permission(user="analyst", resource="pattern", action="execute")
```

### Encryption

```python
from security.encryption import Encryption

enc = Encryption()
encrypted = enc.encrypt("sensitive data")
decrypted = enc.decrypt(encrypted)
```

### Audit Logging

```python
from security.audit_logger import AuditLogger

logger = AuditLogger()
logger.log_action(
    user="user@example.com",
    action="pattern_execution",
    resource="reflection_pattern",
    result="success"
)
```

---

## Monitoring & Evaluation

### Prometheus Metrics

Access metrics at: http://localhost:9090

```python
from monitoring.metrics import pattern_execution_counter

# Metrics automatically tracked:
# - pattern_execution_total
# - pattern_duration_seconds
# - pattern_error_rate
# - active_requests_gauge
```

### Grafana Dashboards

Access dashboards at: http://localhost:3000 (admin/admin)

- Pattern execution trends
- Performance metrics
- Error rates and alerts
- Cost analysis

### Performance Benchmarking

```powershell
# Run benchmarks
python -m evaluation.benchmarks.performance_tests

# Cost analysis
python -m evaluation.benchmarks.cost_analysis

# Accuracy testing
python -m evaluation.benchmarks.accuracy_tests
```

### Evaluation Dashboard

```python
from evaluation.reports.evaluation_dashboard import EvaluationDashboard

dashboard = EvaluationDashboard()
report = dashboard.generate_report({
    "reflection": {"accuracy": 0.95, "latency": 2.3},
    "react": {"accuracy": 0.92, "latency": 3.1}
})
```

---

## Testing

### Run All Tests

```powershell
pytest tests/ -v --cov=patterns --cov=api --cov-report=html
```

### Run Specific Test Suites

```powershell
# Unit tests
pytest tests/unit/ -v

# Integration tests
pytest tests/integration/ -v

# End-to-end tests
pytest tests/e2e/ -v

# Performance tests
pytest tests/performance/ -v
```

### Test Individual Pattern

```powershell
pytest tests/unit/patterns/test_reflection.py -v
```

---

## Documentation

### Comprehensive Guides

- **[Quick Start Guide](QUICKSTART.md)**: Get started in 5 minutes
- **[Getting Started](docs/GETTING_STARTED.md)**: Detailed installation and setup
- **[Deployment Guide](docs/DEPLOYMENT.md)**: Production deployment instructions
- **[Architecture Comparison](docs/ARCHITECTURE_COMPARISON.md)**: Pattern selection guide
- **[API Reference](docs/API_REFERENCE.md)**: Complete API documentation
- **[Contributing Guide](CONTRIBUTING.md)**: Development guidelines
- **[Changelog](CHANGELOG.md)**: Version history

### Pattern Documentation

Each pattern includes:
- Detailed README with use cases
- Example implementations
- Configuration options
- Performance characteristics
- Best practices

Example: `patterns/01_reflection/README.md`

### Interactive Examples

- **Jupyter Notebooks**: `examples/notebooks/`
- **Streamlit Demo**: `examples/demos/streamlit_app.py`
- **CLI Tool**: `examples/demos/cli_demo.py`

---

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-pattern`)
3. Make your changes
4. Add tests
5. Run tests (`pytest tests/ -v`)
6. Commit (`git commit -m 'feat: add amazing pattern'`)
7. Push (`git push origin feature/amazing-pattern`)
8. Open a Pull Request

### Development Setup

```powershell
# Clone your fork
git clone https://github.com/your-username/AWS-AGENTIC-ARCHITECTURES.git

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Run formatting
black patterns/ api/ utils/
flake8 patterns/ api/ utils/
```

## Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/swsarancodes/AWS-AGENTIC-ARCHITECTURES/issues)
- **Discussions**: [GitHub Discussions](https://github.com/swsarancodes/AWS-AGENTIC-ARCHITECTURES/discussions)

---

<div align="center">

[Back to Top](#aws-agentic-architectures)

</div>
