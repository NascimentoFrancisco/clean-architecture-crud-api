from typing import Dict
from abc import ABC, abstractmethod


class SelectUserInterface(ABC):
    """Interface to UserInsert use case"""

    @abstractmethod
    def select(self, user_id: str) -> Dict:
        """abstractmethod"""
