from typing import Dict


class ChangePasswordUserSpy:
    """Spy to ChangePasswordUserInterface usecase:"""

    def __init__(self) -> None:
        self.change_password_attributes = {}

    def change_password(
        self, email: str, new_password: str, password_confirmation: str
    ) -> Dict:
        """Change password"""

        self.change_password_attributes["email"] = email
        self.change_password_attributes["new_password"] = new_password
        self.change_password_attributes["password_confirmation"] = password_confirmation

        return {
            "type": "users",
            "count": 1,
            "id": "fuhfieheryueiruiewi",
            "attributes": {"message": "Senha alterda com sucesso"},
        }
