class AccessControl:
    """Role-based access control."""
    def __init__(self):
        self.roles = {
            "admin": ["read", "write", "delete"],
            "user": ["read", "write"],
            "guest": ["read"]
        }
    
    def check_permission(self, role, action):
        return action in self.roles.get(role, [])
