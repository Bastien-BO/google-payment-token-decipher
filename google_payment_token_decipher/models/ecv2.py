"""
All dataclasses used to represent an ecv2 key-set
"""
from dataclasses import dataclass
from datetime import datetime

from google_payment_token_decipher.models.signed_Key import SignedKey


@dataclass
class Ecv2(SignedKey):
    """
    Ecv2 model
    """

    protocolVersion: str

    def __post_init__(self):
        self.keyExpiration = datetime.fromtimestamp(int(self.keyExpiration) / 1000)