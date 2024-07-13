from src.infra.db.tests import UsersRpositorySpy
from .delete_user import DeleteUser


def test_delte_user():
    """Test with the correct user_id"""

    user_id = "123456sfdfsadfsf"
    user_repository = UsersRpositorySpy()
    delete_user = DeleteUser(user_repository)

    response = delete_user.delete(user_id)

    # Testing input
    assert user_repository.delete_user_attributes["user_id"] == user_id

    # Testing output
    assert response["type"] == "users"
    assert response["count"] == 1
    assert response["attributes"]


def test_delete_user_user_id_invalid():
    """Test with the incorrect user_id"""

    user_id = 123
    user_repository = UsersRpositorySpy()
    delete_user = DeleteUser(user_repository)

    try:
        delete_user.delete(user_id)
        assert False
    except Exception as exception:
        assert str(exception) == "Id inválido, o mesmo deve ser uma string"


def test_delete_user_not_found():
    """Test with non-existent user"""

    user_id = "not found"
    user_repository = UsersRpositorySpy()
    delete_user = DeleteUser(user_repository)

    try:
        delete_user.delete(user_id)
        assert False
    except Exception as exception:
        assert str(exception) == "'NoneType' object has no attribute 'id'"
