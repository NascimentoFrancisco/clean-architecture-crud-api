from src.data.use_cases.insert_user import InsertUser
from src.infra.db.repositories.user_repository import UserRepository
from src.infra.db.services.hashing_service import HashingServise
from src.presentation.controllers import InsertUserController


def insert_user_composer():
    """
    InsertUserController composer
        - parameter:
            * None
        - return:
            * An function handle of InsertUserController
    """

    repository = UserRepository()
    hashing_servise = HashingServise()
    use_case = InsertUser(repository, hashing_servise)
    controller = InsertUserController(use_case)

    return controller.handle
