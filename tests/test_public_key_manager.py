from google_payment_token_decipher import key_manager


def test_retrieve_key_for_production_mode():
    keys = key_manager(production=True, refresh_background=False)
    assert keys.ecv2 is not None
    assert keys.ecv2.protocolVersion == "ECv2"


def test_retrieve_key_for_development_mode():
    keys = key_manager(production=False, refresh_background=False)
    assert keys.ecv2 is not None
    assert keys.ecv2.protocolVersion == "ECv2"

