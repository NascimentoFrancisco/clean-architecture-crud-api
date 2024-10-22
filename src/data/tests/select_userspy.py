class SelectUserSpy:
    """Class to define usecase: SelectUser"""

    def __init__(self) -> None:
        self.select_user_attributes = {}

    def select(self, user_id: str) -> None:
        """Insert user"""
        self.select_user_attributes["user_id"] = user_id

        return {
            "type": "users",
            "count": 1,
            "id": "fuhfieheryueiruiewi",
            "attributes": {"name": "Testes", "email": "teste@teste.com"},
        }
