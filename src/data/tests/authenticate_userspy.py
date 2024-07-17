from typing import Dict


class AuthenticateUserSpy:
    """Spy to AuthenticateUserInterface usecase:"""

    def __init__(self) -> None:
        self.insert_user_attributes = {}

    def authenticate_user(self, email: str, password: str) -> Dict:
        """Insert user"""

        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["password"] = password

        return {
            "type": "users",
            "count": 1,
            "id": "fuhfieheryueiruiewi",
            "attributes": {"name": "Testes", "email": "teste@teste.com"},
        }
