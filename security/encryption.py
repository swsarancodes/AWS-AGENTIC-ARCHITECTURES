from cryptography.fernet import Fernet
import os

class Encryption:
    """Encryption utilities for sensitive data."""
    def __init__(self, key=None):
        self.key = key or os.getenv("ENCRYPTION_KEY", Fernet.generate_key())
        self.cipher = Fernet(self.key)
    
    def encrypt(self, data: str) -> bytes:
        return self.cipher.encrypt(data.encode())
    
    def decrypt(self, encrypted_data: bytes) -> str:
        return self.cipher.decrypt(encrypted_data).decode()
