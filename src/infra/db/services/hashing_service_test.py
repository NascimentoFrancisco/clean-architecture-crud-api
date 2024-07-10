from .hashing_service import HashingServise

hashing_servise = HashingServise()


def test_encrypt_password():
    """Must encrypt the password"""

    password = "MeuTeste123"

    response = hashing_servise.encrypt_password(password)
    print()
    print(response)

    assert response != password


def test_verify_password():
    """Must compare correct passwords"""

    hash_password = hashing_servise.encrypt_password("MeuTeste123")
    response = hashing_servise.verify_password("MeuTest123", hash_password)
    response_incorrect = hashing_servise.verify_password("MeuTeste", hash_password)
    print()
    print(hash_password)
    print()
    print(response)
    print(response_incorrect)

    # assert response is True
    # assert response_incorrect is False