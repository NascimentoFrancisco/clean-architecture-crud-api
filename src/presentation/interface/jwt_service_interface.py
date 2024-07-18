from abc import ABC, abstractmethod
from typing import Dict


class JwtServiceInterface(ABC):
    """Interface to Service responsible for managing jwt authentication"""

    @abstractmethod
    def generate_access_token(self, email: str) -> Dict:
        """abstractmethod"""

    @abstractmethod
    def get_logged_user_identity(self) -> str:
        """abstractmethod"""
