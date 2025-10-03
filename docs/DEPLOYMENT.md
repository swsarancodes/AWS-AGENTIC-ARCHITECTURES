# Deployment Guide

This guide describes how to deploy the AWS Agentic Architectures project in various environments, including local, Docker, and AWS cloud.

## Local Deployment

1. Install dependencies:
   ```bash
   uv sync
   # or
   pip install -r requirements.txt
   ```
2. Start the API server:
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```

## Docker Deployment

1. Build and start all services:
   ```bash
   docker-compose up --build
   ```
2. Access the API at `http://localhost:8000`
3. Access the Streamlit demo at `http://localhost:8501`

## AWS Cloud Deployment

- Use the provided CloudFormation, Terraform, or CDK templates in `infrastructure/aws/` to provision resources.
- Update environment variables and secrets in AWS Secrets Manager.
- Deploy Lambda functions and API Gateway using the templates.

## Kubernetes Deployment

1. Apply manifests in `infrastructure/kubernetes/`:
   ```bash
   kubectl apply -f infrastructure/kubernetes/
   ```
2. Configure ingress and service accounts as needed.

## Monitoring & Logging
- Prometheus and Grafana are included in the Docker Compose setup.
- CloudWatch logging is enabled for AWS Lambda and API Gateway.

## Security
- Use IAM roles and policies for AWS resources.
- Store secrets securely in AWS Secrets Manager or SSM Parameter Store.

## Troubleshooting
- Check logs in the `logs/` directory or CloudWatch.
- Ensure all environment variables are set correctly.
- Verify AWS credentials and permissions.
