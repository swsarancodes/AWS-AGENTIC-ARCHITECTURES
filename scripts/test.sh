#!/bin/bash
# Test script for AWS Agentic Architectures

echo "Running tests..."

pytest tests/ -v --cov=patterns --cov=api --cov-report=html

echo "Tests complete!"
