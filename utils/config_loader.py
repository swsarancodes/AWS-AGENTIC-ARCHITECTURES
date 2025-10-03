import os
from dotenv import load_dotenv

class ConfigLoader:
    """Loads configuration from environment variables and .env files."""
    def __init__(self, env_file=".env"):
        load_dotenv(env_file)
    
    def get(self, key, default=None):
        return os.getenv(key, default)
    
    def get_int(self, key, default=0):
        return int(os.getenv(key, default))
    
    def get_bool(self, key, default=False):
        return os.getenv(key, str(default)).lower() in ("true", "1", "yes")
