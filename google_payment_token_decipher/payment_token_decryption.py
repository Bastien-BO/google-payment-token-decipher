"""

"""
from google_payment_token_decipher import PublicKeyManager


class PaymentTokenDecryption:
    """
    Convert a google payment token into a decryption payment token.

    """

    def __init__(
        self,
        production: bool = False,
        refresh_background: bool = True,
    ):
        """
        Payment token decryption object used to decrypt a Google payment token payload

        Setting refresh_background to False can result in a false positive payment token validation,
        using it cause some delay for every request but insure security, use wisely
        :param production: Choose between production and test environment
        :param refresh_background: Activate Google certificate auto refresh for every request (most secure mode)
        """

        self.public_key_manager: PublicKeyManager = PublicKeyManager(
            production, refresh_background
        )

    def decrypt(self, ):
        """

        :return:
        """
        pass
