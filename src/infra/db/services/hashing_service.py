from passlib.hash import pbkdf2_sha256
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
        hashed = pbkdf2_sha256.hash(raw_password)

        return hashed

    def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        """
        Returns the comparison between the entered password and the encrypted password
            * parameters:
                - raw_password(str): raw user password
                - hashed_password(str): A kind of password hash
            * retrun:
                - True if the attributes are the same, and False if they are not
        """

        return pbkdf2_sha256.verify(raw_password, hashed_password)
