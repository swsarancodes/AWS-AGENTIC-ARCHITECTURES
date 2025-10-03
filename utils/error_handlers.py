import logging

class ErrorHandlers:
    """Centralized error handling utilities."""
    
    @staticmethod
    def handle_bedrock_error(error):
        logging.error(f"Bedrock error: {error}")
        return {"error": "AWS Bedrock service error", "detail": str(error)}
    
    @staticmethod
    def handle_validation_error(error):
        logging.error(f"Validation error: {error}")
        return {"error": "Input validation failed", "detail": str(error)}
