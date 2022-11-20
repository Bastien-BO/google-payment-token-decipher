"""
All dataclasses used to represent an input payment method token structure
"""
import json
from dataclasses import dataclass
from typing import List
from typing import Union


@dataclass
class IntermediateSigningKey:
    """
    Intermediate signing key model
    """

    signedKey: str
    signatures: List[str]


@dataclass
class Signature:
    """
    Payment signature model
    """

    keyExpiration: str
    keyValue: str


@dataclass
class PaymentMethodToken:
    """
    Payment method token model
    """

    protocolVersion: str
    signature: Union[Signature, str]
    intermediateSigningKey: Union[IntermediateSigningKey, dict]
    signedMessage: str

    def __post_init__(self):
        self.signature = Signature(**json.loads(self.signature))
        self.intermediateSigningKey = IntermediateSigningKey(
            **self.intermediateSigningKey
        )
