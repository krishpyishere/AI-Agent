import jwt
from datetime import datetime, timedelta
from typing import Dict, Optional

class AuthManager:
    def __init__(self, secret_key: str = "your-secret-key"):
        self.secret_key = secret_key
        self.users: Dict = {}  # In production, use a proper database

    def create_user(self, username: str, password: str) -> Dict:
        """Create a new user."""
        if username in self.users:
            raise ValueError("Username already exists")
        
        user_id = str(len(self.users) + 1)
        self.users[username] = {
            "id": user_id,
            "password": password  # In production, hash the password
        }
        
        return {"user_id": user_id, "username": username}

    def generate_token(self, username: str, password: str) -> Optional[str]:
        """Generate JWT token for authentication."""
        if username not in self.users or self.users[username]["password"] != password:
            return None
        
        payload = {
            "user_id": self.users[username]["id"],
            "exp": datetime.utcnow() + timedelta(hours=24)
        }
        
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def is_authorized(self, token: str) -> bool:
        """Verify if the token is valid."""
        try:
            jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return True
        except jwt.InvalidTokenError:
            return False 