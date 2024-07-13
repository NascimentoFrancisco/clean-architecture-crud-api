class DeleteUserSpy:
    """Class to define usecase: DeleteUser"""

    def __init__(self) -> None:
        self.delete_user_attributes = {}

    def delete(self, user_id: str) -> None:
        """Insert user"""
        self.delete_user_attributes["user_id"] = user_id

        return {
            "type": "users",
            "count": 1,
            "id": "fuhfieheryueiruiewi",
            "attributes": {"name": "Testes", "email": "teste@teste.com"},
        }
