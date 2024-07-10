class Users:
    """Class representing Users"""

    def __init__(
        self, name: str, email: str, password: str, user_id: str = None
    ) -> None:
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
