#!/bin/bash
# Cleanup script for AWS Agentic Architectures

echo "Cleaning up..."

# Remove temporary files
rm -rf __pycache__
rm -rf .pytest_cache
rm -rf htmlcov
rm -rf *.egg-info
rm -rf .mypy_cache

echo "Cleanup complete!"
