from abc import ABC, abstractmethod
from src.domain.entites import Users


class AuthenticateUserInterface(ABC):
    """Interface to AuthenticateUser use case"""

    @abstractmethod
    def authenticate_user(self, email: str, password: str) -> Users:
        """abstractmethod"""
