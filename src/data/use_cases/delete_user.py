from typing import Dict, Type
from src.domain.use_cases import DeleteUserInterface
from src.data.interfaces import UserRepositoryInterface
from src.domain.entites import Users
from src.errors.types import HttpBadRequestError


class DeleteUser(DeleteUserInterface):
    """Class that implements the DeleteUser use case"""

    def __init__(self, delete_user_repository: Type[UserRepositoryInterface]) -> None:
        self.__delete_user_repository = delete_user_repository

    def delete(self, user_id: str) -> Dict:
        self.__validate_user_id(user_id)
        user_deleted = self.__delete_user(user_id)
        return self.__format_response(user_deleted)

    @classmethod
    def __validate_user_id(cls, user_id: str) -> None:
        if not isinstance(user_id, str):
            raise HttpBadRequestError("Id inválido, o mesmo deve ser uma string")

    def __delete_user(self, user_id: str) -> bool:
        user_deleted = self.__delete_user_repository.delete_user(user_id)
        return user_deleted

    @classmethod
    def __format_response(cls, user: Type[Users]) -> Dict:
        response = {
            "type": "users",
            "count": 1,
            "id": user.id,
            "attributes": {"message": f"Usuário {user.name} excluído com sucesso"},
        }
        return response
