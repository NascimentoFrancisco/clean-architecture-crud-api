from abc import ABC, abstractmethod
from src.domain.entites import Users


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_user(self, name: str, email: str, password: str) -> Users:
        """abstractmethod"""

    @abstractmethod
    def select_user(self, user_id: str) -> Users:
        """abstractmethod"""

    @abstractmethod
    def select_user_by_email(self, email: str) -> Users:
        """abstractmethod"""

    @abstractmethod
    def update_user(self, user_id: str, **kwargs) -> Users:
        """abstractmethod"""

    @abstractmethod
    def delete_user(self, user_id: str) -> Users:
        """abstractmethod"""

    @abstractmethod
    def change_password_user(self, email: str, new_password: str) -> Users:
        """abstractmethod"""
