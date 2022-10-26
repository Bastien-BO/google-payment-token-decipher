"""
All exception classes used in google payment token decipher
"""


class GooglePaymentTokenDecipherError(BaseException):
    """
    Global Error for Google payment token decipher
    """


class PublicKeyManagerError(GooglePaymentTokenDecipherError):
    """
    Global Error for the public key manager
    """


class GetPublicKeySetsError(PublicKeyManagerError):
    """
    Error while fetching google public key-sets
    """


class GetEcv2KeySetError(PublicKeyManagerError):
    """
    Unable to retrieve Ecv2 key-set from google public key-sets
    """
