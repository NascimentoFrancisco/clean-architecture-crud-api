from src.domain.tests import user_mocks


class UsersRpositorySpy:
    """Spy to User Repository"""

    def __init__(self) -> None:
        self.insert_user_attributes = {}

    def insert_user(self, name: str, email: str, password: str) -> None:
        """Spy to all attributes"""
        self.insert_user_attributes["name"] = name
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["password"] = password

        return user_mocks()
