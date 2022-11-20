"""

"""
from dataclasses import dataclass


@dataclass
class PaymentMethodDetails:
    """
    Payment method details model
    """

    authMethod: str
    pan: str
    expirationMonth: int
    expirationYear: int


@dataclass
class PaymentMethodDetails3ds(PaymentMethodDetails):
    """
    Payment method details 3ds model
    """

    cryptogram: str
    eciIndicator: str
