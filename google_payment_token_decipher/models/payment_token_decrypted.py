"""
All dataclasses used to represent a pan only decrypted payload
"""
from dataclasses import dataclass
from typing import Union

from google_payment_token_decipher.models.payment_method_details import (
    PaymentMethodDetails,
)


@dataclass
class PaymentTokenDecrypted:
    """
    Pan only model
    """

    paymentMethod: str
    gatewayMerchantId: str
    messageId: str
    messageExpiration: Union[int, str]

    def __post_init__(self):
        self.messageExpiration = int(self.messageExpiration)
