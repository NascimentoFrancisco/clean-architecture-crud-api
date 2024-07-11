from src.domain.entites import Users


def user_mocks():
    """Mocking Users"""
    return Users(user_id=1, name="user", email="email@email.com", password="password")
