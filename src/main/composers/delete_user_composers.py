from src.data.use_cases.delete_user import DeleteUser
from src.infra.db.repositories.user_repository import UserRepository
from src.presentation.controllers import DeleteUserController


def delete_user_composer():
    """
    DeleteUserController composer
        - parameter:
            * None
        - return:
            * An function handle of DeleteUserController
    """
    repository = UserRepository()
    use_case = DeleteUser(repository)
    controller = DeleteUserController(use_case)

    return controller.handle
