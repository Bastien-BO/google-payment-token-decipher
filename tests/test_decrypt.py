from random import randint

from google_payment_token_decipher.payment_token_decryption import PaymentTokenDecryption


def test_error_decrypt_int():
    test = PaymentTokenDecryption()
    assert test.decrypt(100)