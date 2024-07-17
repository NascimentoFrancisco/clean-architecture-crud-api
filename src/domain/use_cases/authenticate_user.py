from abc import ABC, abstractmethod


class AuthenticateUserInterface(ABC):
    """Interface to AuthenticateUser use case"""

    @abstractmethod
    def authenticate_user(self, email: str, password: str) -> None:
        """abstractmethod"""
