from abc import ABC, abstractmethod


class UserInsertInterface(ABC):
    """Interface to UserInsert use case"""

    @abstractmethod
    def insert(self, name: str, email: str, password: str) -> None:
        """abstractmethod"""
