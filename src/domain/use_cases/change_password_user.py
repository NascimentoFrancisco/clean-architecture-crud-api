from typing import Dict
from abc import ABC, abstractmethod


class ChangePasswordUserInterface(ABC):
    """Interface to ChangePasswordUser use case"""

    @abstractmethod
    def change_password(
        self, email: str, new_password: str, password_confirmation: str
    ) -> Dict:
        """abstractmethod"""
