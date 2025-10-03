# API Reference

This document describes the REST API endpoints for interacting with agentic patterns and utilities in the AWS Agentic Architectures project.

## Base URL
```
http://localhost:8000
```

## Endpoints

### Health Check
- `GET /health`
  - Returns API health status.

### List Patterns
- `GET /patterns`
  - Returns a list of available agentic patterns.

### Run Pattern
- `POST /patterns/{pattern_name}/run`
  - Runs the specified pattern with input data.
  - Request body: `{ "input": "..." }`
  - Response: `{ "output": "..." }`

### Pattern Details
- `GET /patterns/{pattern_name}`
  - Returns details and configuration for a specific pattern.

### Evaluation
- `POST /evaluation/run`
  - Runs evaluation benchmarks on selected patterns.
  - Request body: `{ "patterns": ["reflection", "react"], "dataset": "..." }`

### Monitoring
- `GET /metrics`
  - Returns Prometheus metrics for monitoring.

## Authentication
- API key header: `X-API-Key: your-api-key`
- JWT bearer token: `Authorization: Bearer <token>`

## Error Handling
- Standardized error responses with code and message.

## Example Request
```bash
curl -X POST http://localhost:8000/patterns/reflection/run \
  -H "Content-Type: application/json" \
  -d '{"input": "Review this code for bugs."}'
```

Refer to the FastAPI OpenAPI docs at `/docs` for interactive API exploration.
