import logging
from datetime import datetime

class AuditLogger:
    """Audit logging for compliance."""
    def __init__(self):
        self.logger = logging.getLogger("audit")
    
    def log_action(self, user, action, resource):
        self.logger.info(f"{datetime.now()} | User: {user} | Action: {action} | Resource: {resource}")
