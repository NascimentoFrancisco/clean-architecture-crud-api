class HashingServiseSpy:
    """Spy to User HashingServise"""

    def __init__(self) -> None:
        self.encrypt_password_attributes = {}
        self.verify_password_attributes = {}

    def encrypt_password(self, raw_password: str) -> str:
        """Spy to all attributes"""
        self.encrypt_password_attributes["encrypt_password"] = raw_password

    def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        """Spy to all attributes"""
        self.verify_password_attributes["raw_password"] = raw_password
        self.verify_password_attributes["hashed_password"] = hashed_password

        if raw_password != hashed_password:
            return False

        return True
