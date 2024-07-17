from src.domain.tests import user_mocks
from src.domain.entites import Users


class UsersRpositorySpy:
    """Spy to User Repository"""

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}
        self.select_user_by_email_attributes = {}
        self.update_user_attributes = {}
        self.delete_user_attributes = {}

    def insert_user(self, name: str, email: str, password: str) -> Users:
        """Spy to all attributes"""
        self.insert_user_attributes["name"] = name
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["password"] = password

        return user_mocks()

    def select_user(self, user_id: str) -> Users | None:
        """Spy to all attributes"""

        if user_id == "not found":
            return None

        self.select_user_attributes["user_id"] = user_id

        return user_mocks()

    def select_user_by_email(self, email: str) -> Users | None:
        """Spy to all attributes"""

        if email == "not found":
            return None

        self.select_user_by_email_attributes["email"] = email

        return user_mocks()

    def update_user(self, user_id: str, **kwargs) -> Users:
        """Spy to all attributes"""
        self.update_user_attributes["user_id"] = user_id

        if "name" in kwargs:
            self.update_user_attributes["name"] = kwargs["name"]

        if "email" in kwargs:
            self.update_user_attributes["email"] = kwargs["email"]

        return user_mocks()

    def delete_user(self, user_id: str) -> bool | None:
        """Spy to all attributes"""

        if user_id == "not found":
            return None

        self.delete_user_attributes["user_id"] = user_id

        return user_mocks()
