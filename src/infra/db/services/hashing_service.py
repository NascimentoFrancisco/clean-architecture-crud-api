import os
import hashlib
from src.domain.use_cases import HashingServiseInterface


class HashingServise(HashingServiseInterface):
    """Class that implements User password encryption"""

    def encrypt_password(self, raw_password: str) -> str:
        """
        Returns the encrypted user password
            * parameters:
                - raw_password(str): raw user password
            * retrun:
                - A kind of password hash
        """
        salt = os.urandom(32)
        hash_object = hashlib.sha256()
        hash_object.update(salt + raw_password.encode())
        hash_password = hash_object.hexdigest()

        return hash_password

    def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        """
        Returns the comparison between the entered password and the encrypted password
            * parameters:
                - raw_password(str): raw user password
                - hashed_password(str): A kind of password hash
            * retrun:
                - True if the attributes are the same, and False if they are not
        """
        salt = os.urandom(32)
        hash_object = hashlib.sha256()
        hash_object.update(salt + raw_password.encode())
        hash_password = hash_object.hexdigest()

        return hash_password == hashed_password
