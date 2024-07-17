from typing import Dict


class JwtServiceSpy:
    """SPY to tests"""

    def __init__(self) -> None:
        self.jwt_attributes = {}

    def generate_access_token(self, email: str) -> Dict:
        """Method spy to test"""
        self.jwt_attributes["email"] = email

        return {"access_token": "access_token"}
