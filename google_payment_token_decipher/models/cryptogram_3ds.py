"""
All cryptogram 3ds related models
"""
from dataclasses import dataclass
from typing import Union

from google_payment_token_decipher.models.payment_method_details import (
    PaymentMethodDetails3ds,
)
from google_payment_token_decipher.models.payment_token_decrypted import (
    PaymentTokenDecrypted,
)


@dataclass
class Cryptogram3ds(PaymentTokenDecrypted):
    """
    Cryptogram 3ds model
    """

    paymentMethodDetails: Union[PaymentMethodDetails3ds, dict]

    def __post_init__(self):
        super(Cryptogram3ds, self).__post_init__()
        self.paymentMethodDetails = PaymentMethodDetails3ds(**self.paymentMethodDetails)
