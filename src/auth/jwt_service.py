from typing import Dict
from flask_jwt_extended import create_access_token
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
        print(access_token)
        return {"access_token": access_token}
