from pydantic import BaseModel, ValidationError

class Validators:
    """Common validators for input data."""
    
    @staticmethod
    def validate_model_id(model_id: str) -> bool:
        """Validate Bedrock model ID format."""
        valid_prefixes = ["anthropic.", "amazon.", "meta.", "cohere."]
        return any(model_id.startswith(prefix) for prefix in valid_prefixes)
    
    @staticmethod
    def validate_region(region: str) -> bool:
        """Validate AWS region."""
        valid_regions = ["us-east-1", "us-west-2", "eu-west-1", "ap-southeast-1"]
        return region in valid_regions
