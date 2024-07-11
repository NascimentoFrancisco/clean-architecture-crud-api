from typing import Type
from abc import ABC, abstractmethod
from src.presentation.http_types import HttpRequest, HttpResponse


class ControllerInterface(ABC):
    """Class that defines rules for controllers"""

    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """abstractmethod"""
