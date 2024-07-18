from src.data.use_cases.change_password_user import ChangePasswordUser
from src.presentation.controllers import ChangePasswordUserController
from src.infra.db.repositories.user_repository import UserRepository
from src.infra.db.services.hashing_service import HashingServise
from src.auth import JwtService


def change_password_user_composer():
    """
    ChangePasswordUserController composer
        - parameter:
            * None
        - return:
            * An function handle of ChangePasswordUserController
    """
    repository = UserRepository()
    hashing_servise = HashingServise()
    use_case = ChangePasswordUser(repository, hashing_servise)
    jwt_service = JwtService()
    controller = ChangePasswordUserController(use_case, jwt_service)

    return controller.handle
