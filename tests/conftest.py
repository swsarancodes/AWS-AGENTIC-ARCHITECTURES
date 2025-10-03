import pytest
from patterns.base.bedrock_client import BedrockClient

@pytest.fixture
def bedrock_client():
    return BedrockClient(region="us-east-1")

@pytest.fixture
def sample_config():
    return {
        "region": "us-east-1",
        "model_id": "anthropic.claude-3-sonnet-20240229-v1:0"
    }
