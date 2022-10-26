"""
Public key manager
"""
from functools import lru_cache

import requests
from requests import RequestException

from google_payment_token_decipher.exceptions import GetEcv2KeySetError
from google_payment_token_decipher.exceptions import GetPublicKeySetsError
from google_payment_token_decipher.models import Ecv2


class PublicKeyManager:
    """
    container for
    """

    __KEYS_URL_PRODUCTION: str = (
        "https://payments.developers.google.com/paymentmethodtoken/keys.json"
    )
    __KEYS_URL_TEST: str = (
        "https://payments.developers.google.com/paymentmethodtoken/test/keys.json"
    )

    def __init__(self, production: bool = False, refresh_background: bool = False):
        self.__production = production
        self.__refresh_background = refresh_background
        self.data = self.get_keyset()

    def refresh_keyset(self):
        """
        Force lru reload
        """
        ...

    def get_keyset(self) -> Ecv2:
        """
        get google payment method token key-set converted to Ecv2 object
        """
        try:
            response = requests.get(
                self.__KEYS_URL_PRODUCTION
                if self.__production
                else self.__KEYS_URL_TEST
            ).json()
            return Ecv2(
                **next(
                    (
                        key_set
                        for key_set in response["keys"]
                        if key_set["protocolVersion"] == "ECv2"
                    ),
                )
            )
        except RequestException as err:
            raise GetPublicKeySetsError from err
        except StopIteration as err:
            raise GetEcv2KeySetError from err

    @lru_cache
    def get_public_key(self):
        return self.refresh_keyset()
