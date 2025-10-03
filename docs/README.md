# AWS Agentic Architectures
AWS Agentic Architectures Documentation

This documentation provides detailed guides, architecture comparisons, deployment instructions, and API references for the 17 agentic patterns built on AWS Bedrock.

## Contents
- [Getting Started](GETTING_STARTED.md)
- [Deployment Guide](DEPLOYMENT.md)
- [Architecture Comparison](ARCHITECTURE_COMPARISON.md)
- [API Reference](API_REFERENCE.md)

Refer to each section for in-depth explanations and practical usage examples.
A comprehensive collection of 17 production-ready agentic AI patterns built on AWS Bedrock, designed for enterprise deployment and scalability.

## Overview

This repository provides battle-tested implementations of agentic AI architectures, each optimized for specific use cases and built using AWS Bedrock as the foundational LLM service. From simple reflection patterns to complex multi-agent systems, these blueprints enable rapid development and deployment of intelligent automation solutions.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/swsarancodes/AWS-AGENTIC-ARCHITECTURES.git
cd AWS-AGENTIC-ARCHITECTURES

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure

# Run a simple example
python patterns/01_reflection/example.py
```

## Architecture Patterns

| Pattern | Use Case | Complexity | Best For |
|---------|----------|------------|----------|
| [Reflection](patterns/01_reflection/) | Code generation with self-review | Low | Quality-critical outputs |
| [Tool Using](patterns/02_tool_using/) | Customer support chatbot | Low | External system integration |
| [ReAct](patterns/03_react/) | Investigative research | Medium | Multi-step reasoning |
| [Planning](patterns/04_planning/) | Workflow automation | Medium | Sequential processes |
| [PEV](patterns/05_pev/) | API data extraction | Medium | Error-prone environments |
| [Tree of Thoughts](patterns/06_tree_of_thoughts/) | Route optimization | High | Combinatorial problems |
| [Multi-Agent](patterns/07_multi_agent/) | Market analysis | High | Complex collaborative tasks |
| [Meta-Controller](patterns/08_meta_controller/) | Enterprise helpdesk | Medium | Multi-domain routing |
| [Blackboard](patterns/09_blackboard/) | Incident response | High | Dynamic collaboration |
| [Ensemble](patterns/10_ensemble/) | Investment decisions | Medium | High-stakes choices |
| [Episodic+Semantic Memory](patterns/11_episodic_semantic_memory/) | Fitness coaching | High | Personalization |
| [Graph Memory](patterns/12_graph_memory/) | Supply chain intelligence | High | Relational queries |
| [Self-Improvement](patterns/13_self_improvement/) | Content moderation | Medium | Iterative quality |
| [Dry-Run Harness](patterns/14_dry_run_harness/) | Email campaigns | Low | Safety-critical actions |
| [Simulator](patterns/15_simulator/) | Algorithmic trading | High | Risk assessment |
| [Reflexive Metacognitive](patterns/16_reflexive_metacognitive/) | Legal advice | Medium | Boundary enforcement |
| [Cellular Automata](patterns/17_cellular_automata/) | Warehouse robotics | High | Spatial coordination |

## Project Structure

```
AWS-AGENTIC-ARCHITECTURES/
├── patterns/           # 17 agentic patterns with examples
├── infrastructure/     # AWS deployment configurations
├── api/               # REST API for pattern execution
├── evaluation/        # Benchmarking and metrics
├── examples/          # Use case demonstrations
├── monitoring/        # Observability and logging
├── security/          # Security and compliance
└── utils/            # Shared utilities
```

## Key Features

- **Production Ready**: Includes Docker, Kubernetes, and AWS infrastructure configurations
- **Comprehensive Testing**: Unit, integration, and performance tests for all patterns
- **Monitoring & Observability**: Built-in metrics, logging, and alerting
- **Security First**: Encryption, access control, and audit logging
- **Scalable Architecture**: Microservices-ready with API gateway integration
- **Cost Optimized**: Efficient resource usage and cost analysis tools

## Prerequisites

- AWS Account with Bedrock access
- Python 3.9+
- AWS CLI configured
- Docker (optional, for containerized deployment)

## Installation

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure AWS credentials**:
   ```bash
   aws configure
   ```

3. **Enable Bedrock models** (if not already done):
   ```bash
   aws bedrock put-model-invocation-logging-configuration --logging-config destinationConfig="{cloudWatchConfig={logGroupName=bedrock-model-invocations,roleArn=arn:aws:iam::YOUR_ACCOUNT:role/service-role/AmazonBedrockExecutionRoleForCloudWatchLogs}}"
   ```

## Documentation

- [Getting Started Guide](docs/GETTING_STARTED.md)
- [Architecture Comparison](docs/ARCHITECTURE_COMPARISON.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [API Reference](docs/API_REFERENCE.md)

## Examples

Explore practical implementations in the [examples](examples/) directory:

- **Customer Support Bot**: Multi-pattern customer service automation
- **Code Generation Pipeline**: Automated code review and deployment
- **Research Assistant**: Intelligent information gathering and synthesis
- **Trading Bot**: Risk-aware algorithmic trading system

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.


## Support

- Documentation: [docs/](docs/)
- Issues: [GitHub Issues](https://github.com/swsarancodes/AWS-AGENTIC-ARCHITECTURES/issues)
- Discussions: [GitHub Discussions](https://github.com/swsarancodes/AWS-AGENTIC-ARCHITECTURES/discussions)

## Acknowledgments

Built with:
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [LangChain](https://langchain.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [FastAPI](https://fastapi.tiangolo.com/)