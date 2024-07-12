from abc import ABC, abstractmethod
from src.domain.entites import Users


class SelectUserInterface(ABC):
    """Interface to UserInsert use case"""

    @abstractmethod
    def select(self, user_id: str) -> Users:
        """abstractmethod"""
