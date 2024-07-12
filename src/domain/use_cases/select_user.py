from typing import Dict
from abc import ABC, abstractmethod


class SelectUserInterface(ABC):
    """Interface to SelectUser use case"""

    @abstractmethod
    def select(self, user_id: str) -> Dict:
        """abstractmethod"""
