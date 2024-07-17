import re
from typing import Type, Dict
from src.domain.use_cases import AuthenticateUserInterface
from src.data.interfaces import UserRepositoryInterface
from src.domain.use_cases import HashingServiseInterface
from src.errors.types import HttpBadRequestError, HttpUnauthorizedError
from src.domain.entites import Users


class AuthenticateUser(AuthenticateUserInterface):
    """Class that implements the AuthenticateUser use case"""

    def __init__(
        self,
        user_repository: Type[UserRepositoryInterface],
        hashing_service: Type[HashingServiseInterface],
    ) -> None:
        self.__user_repository = user_repository
        self.__hashing_service = hashing_service

    def authenticate_user(self, email: str, password: str) -> Dict:
        self.__validate_email(email)
        user = self.__search_user(email)

        if self.__hashing_service.verify_password(password, user.password):
            return self.__format_response(user)

        raise HttpUnauthorizedError(
            "Credenciais fornecidas (email e senha) são inválidas"
        )

    @classmethod
    def __validate_email(cls, email: str):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise HttpBadRequestError("Email inválido")

    def __search_user(self, email: str) -> Users:
        return self.__user_repository.select_user_by_email(email)

    @classmethod
    def __format_response(cls, user: Type[Users]) -> Dict:
        response = {
            "type": "users",
            "count": 1,
            "id": user.id,
            "attributes": {"name": user.name, "email": user.email},
        }
        return response
