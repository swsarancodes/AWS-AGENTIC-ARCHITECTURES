#!/bin/bash
# Setup script for AWS Agentic Architectures

echo "Setting up AWS Agentic Architectures..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Configure AWS CLI
echo "Configuring AWS CLI..."
aws configure

# Create necessary directories
mkdir -p logs
mkdir -p data

echo "Setup complete!"
