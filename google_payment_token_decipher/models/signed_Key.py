"""
All dataclasses used to represent an ecv2 key-set
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Union


@dataclass
class SignedKey:
    """
    SignedKey model
    """

    keyValue: str
    keyExpiration: Union[datetime, str]
