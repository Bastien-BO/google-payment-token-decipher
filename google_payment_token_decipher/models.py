"""
All dataclasses used payment token decipher
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Union


@dataclass
class Ecv2:
    """
    Ecv2 data model
    """

    keyValue: str
    protocolVersion: str
    keyExpiration: Union[datetime, str]

    def __post_init__(self):
        self.keyExpiration = datetime.fromtimestamp(int(self.keyExpiration) / 1000)
