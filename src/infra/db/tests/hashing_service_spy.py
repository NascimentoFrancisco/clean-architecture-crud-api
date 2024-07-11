class HashingServiseSpy:
    """Spy to User HashingServise"""

    def __init__(self) -> None:
        self.encrypt_password_attributes = {}

    def encrypt_password(self, raw_password: str) -> str:
        """Spy to all attributes"""
        self.encrypt_password_attributes["encrypt_password"] = raw_password
