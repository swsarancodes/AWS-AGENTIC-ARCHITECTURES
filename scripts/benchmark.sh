#!/bin/bash
# Benchmark script for AWS Agentic Architectures

echo "Running benchmarks..."

python -m evaluation.benchmarks.performance_tests
python -m evaluation.benchmarks.accuracy_tests
python -m evaluation.benchmarks.cost_analysis

echo "Benchmarks complete!"
