from typing import Dict, Type
from src.domain.entites.users import Users
from src.domain.use_cases import SelectUserInterface
from src.data.interfaces import UserRepositoryInterface
from src.errors.types import HttpBadRequestError, HttpNotFoundError


class SelectUser(SelectUserInterface):
    """Class that implements the SelectUser use case"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:
        self.__user_repository = user_repository

    def select(self, user_id: str) -> Dict:
        self.__validate_user_id(user_id)
        user = self.__search_user(user_id)
        return self.__format_response(user)

    @classmethod
    def __validate_user_id(cls, user_id: str) -> None:
        if not isinstance(user_id, str):
            raise HttpBadRequestError("Id inválido, o mesmo deve ser uma string")

    def __search_user(self, user_id: str) -> Users:
        user = self.__user_repository.select_user(user_id)
        if user is None:
            raise HttpNotFoundError("Usuário não encontrado")
        return user

    @classmethod
    def __format_response(cls, user: Type[Users]) -> Dict:
        response = {
            "type": "users",
            "count": 1,
            "id": user.id,
            "attributes": {"name": user.name, "email": user.email},
        }
        return response
