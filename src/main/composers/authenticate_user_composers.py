from src.data.use_cases.authenticate_user import AuthenticateUser
from src.infra.db.repositories.user_repository import UserRepository
from src.presentation.controllers import AuthenticateUserController
from src.infra.db.services.hashing_service import HashingServise
from src.auth import JwtService


def authenticate_user_composer():
    """
    AuthenticateUserController composer
        - parameter:
            * None
        - return:
            * An function handle of AuthenticateUserController
    """
    repository = UserRepository()
    hashing_servise = HashingServise()
    use_case = AuthenticateUser(repository, hashing_servise)
    jwt_service = JwtService()
    controller = AuthenticateUserController(use_case, jwt_service)

    return controller.handle
