from typing import Dict
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from src.presentation.interface import JwtServiceInterface


class JwtService(JwtServiceInterface):
    """Service responsible for managing jwt authentication"""

    def generate_access_token(self, email: str) -> Dict:
        """Method to generate access token
        * parameters:
                - email(str): user email found
            * retrun:
                - An object of the Dict
        """
        access_token = create_access_token(identity=email)
        return {"access_token": access_token}

    def get_logged_user_identity(self) -> str:
        """Obtains the email/identity of the logged in user
        * parameters:
                - None
            * retrun:
                - An object of the str
        """
        current_user = get_jwt_identity()
        return current_user
