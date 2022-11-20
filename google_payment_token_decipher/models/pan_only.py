"""
All dataclasses used to represent a pan only decrypted payload
"""
from dataclasses import dataclass
from typing import Union

from google_payment_token_decipher.models.payment_method_details import (
    PaymentMethodDetails,
)
from google_payment_token_decipher.models.payment_token_decrypted import (
    PaymentTokenDecrypted,
)


@dataclass
class PanOnly(PaymentTokenDecrypted):
    """
    Pan only model
    """

    paymentMethodDetails: Union[PaymentMethodDetails, dict]

    def __post_init__(self):
        super(PanOnly, self).__post_init__()
        self.paymentMethodDetails = PaymentMethodDetails(**self.paymentMethodDetails)
