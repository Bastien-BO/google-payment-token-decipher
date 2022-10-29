"""
Public key manager
"""
from functools import lru_cache

import requests

from google_payment_token_decipher.exceptions import GetEcv2KeySetError
from google_payment_token_decipher.exceptions import GetPublicKeySetsError
from google_payment_token_decipher.models import Ecv2

__all__ = [
    "key_manager",
    "PublicKeyManager",
]


class PublicKeyManager:
    """
    Public key manager
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
        self.ecv2 = self.__retrive_keyset()

    def refresh_keyset(self) -> None:
        """
        Force refresh the keyset
        """
        self.ecv2 = self.__retrive_keyset()

    def __retrive_keyset(self) -> Ecv2:
        """
        Get google payment method token key-set converted to Ecv2 object
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
        except requests.RequestException as err:
            raise GetPublicKeySetsError from err
        except StopIteration as err:
            raise GetEcv2KeySetError from err

    def keyset(self) -> Ecv2:
        """
        Return the loaded key-set or refresh and return it if refresh background is set
        """
        if self.__refresh_background:
            self.__retrive_keyset()
        return self.ecv2


@lru_cache()
def key_manager(
    production: bool = False, refresh_background: bool = False
) -> PublicKeyManager:
    """
    Get a cached instance of the public key manager
    """
    return PublicKeyManager(production, refresh_background)
