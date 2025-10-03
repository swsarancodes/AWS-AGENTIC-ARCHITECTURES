# Getting Started

Welcome to AWS Agentic Architectures! This guide will help you set up your environment, install dependencies, and run your first agentic pattern using AWS Bedrock.

## Prerequisites
- AWS account with Bedrock access
- Python 3.10+
- Docker (optional, for containerized deployment)
- AWS CLI configured

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/swsarancodes/AWS-AGENTIC-ARCHITECTURES.git
   cd AWS-AGENTIC-ARCHITECTURES
   ```

2. **Install dependencies**
   ```bash
   uv sync
   # or
   pip install -r requirements.txt
   ```

3. **Configure AWS credentials**
   ```bash
   aws configure
   ```

4. **Set environment variables**
   Copy `.env.example` to `.env` and update values as needed.
   ```bash
   cp .env.example .env
   ```

## Running an Example

To run the Reflection pattern example:
```bash
python patterns/01_reflection/example.py
```

## Next Steps
- Explore other patterns in the `patterns/` directory
- Review deployment options in [DEPLOYMENT.md](DEPLOYMENT.md)
- See architecture comparisons in [ARCHITECTURE_COMPARISON.md](ARCHITECTURE_COMPARISON.md)
