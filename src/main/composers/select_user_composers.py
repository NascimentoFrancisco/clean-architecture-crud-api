from src.data.use_cases.select_user import SelectUser
from src.infra.db.repositories.user_repository import UserRepository
from src.presentation.controllers import SelectUserController


def select_user_composer():
    """
    SelectUserController composer
        - parameter:
            * None
        - return:
            * An function handle of SelectUserController
    """
    repository = UserRepository()
    use_case = SelectUser(repository)
    controller = SelectUserController(use_case)

    return controller.handle
