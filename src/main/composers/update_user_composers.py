from src.data.use_cases.update_user import UpdateUser
from src.infra.db.repositories.user_repository import UserRepository
from src.presentation.controllers import UpdateUserController


def update_user_composer():
    """
    UpdateUserController composer
        - parameter:
            * None
        - return:
            * An function handle of UpdateUserController
    """

    repository = UserRepository()
    use_case = UpdateUser(repository)
    controller = UpdateUserController(use_case)

    return controller.handle
