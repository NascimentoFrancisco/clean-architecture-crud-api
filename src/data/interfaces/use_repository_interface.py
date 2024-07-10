from abc import ABC, abstractmethod
from src.domain.entites import Users


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_user(self, name: str, email: str, password: str) -> Users:
        """abstractmethod"""