"""

"""
from google_payment_token_decipher import PublicKeyManager


class PaymentTokenDecipher:
    """ """

    def __init__(
        self,
        production: bool = False,
        refresh_background: bool = True,
    ):
        """
        Payment token decipher object used to decrypt a Google payment token payload

        By setting refresh_background to False can result in a false positive payment token validation,
        using it cause some delay for every request but insure security, use wisely
        Args:
            production: Choose between production and test environment
            refresh_background: Activate Google certificate auto refresh for every request
        """

        self.public_key_manager: PublicKeyManager = PublicKeyManager(
            production, refresh_background
        )
