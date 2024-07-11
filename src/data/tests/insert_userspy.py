class InsertUserSpy:
    """Class to define usecase: InsertUser"""

    def __init__(self) -> None:
        self.insert_user_attributes = {}

    def insert(self, name: str, email: str, password: str) -> None:
        """Insert user"""
        self.insert_user_attributes["name"] = name
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["password"] = password

        return {
            "type": "users",
            "count": 1,
            "id": "fuhfieheryueiruiewi",
            "attributes": {"name": "Testes", "email": "teste@teste.com"},
        }
