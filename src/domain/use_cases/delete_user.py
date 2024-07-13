from typing import Dict
from abc import ABC, abstractmethod


class DeleteUserInterface(ABC):
    """Interface to DeleteUser use case"""

    @abstractmethod
    def delete(self, user_id: str) -> Dict:
        """abstractmethod"""
