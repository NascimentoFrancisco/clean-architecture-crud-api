from typing import Dict
from abc import ABC, abstractmethod


class UpdateUserInterface(ABC):
    """Interface to UpdateUser use case"""

    @abstractmethod
    def update(self, user_id: str, **kwargs) -> Dict:
        """abstractmethod"""
