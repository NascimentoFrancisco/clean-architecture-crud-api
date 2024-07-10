from abc import ABC, abstractmethod


class HashingServiseInterface(ABC):
    """Interface for password encryption"""

    @abstractmethod
    def encrypt_password(self, raw_password: str) -> str:
        """abstractmethod"""

    @abstractmethod
    def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        """abstractmethod"""
