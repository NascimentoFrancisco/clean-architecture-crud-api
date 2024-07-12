class UpdateUserSpy:
    """Class to define usecase: Update"""

    def __init__(self) -> None:
        self.update_user_attributes = {}

    def update(self, user_id: str, **kwargs) -> None:
        """Update user"""
        self.update_user_attributes["user_id"] = user_id

        if "name" in kwargs:
            self.update_user_attributes["name"] = kwargs["name"]

        if "email" in kwargs:
            self.update_user_attributes["email"] = kwargs["email"]

        return {
            "type": "users",
            "count": 1,
            "id": "fuhfieheryueiruiewi",
            "attributes": {"name": "Testes", "email": "teste@teste.com"},
        }
