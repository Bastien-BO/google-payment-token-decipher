"""

"""
import base64
import json
import time
from typing import Union, List

from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

from google_payment_token_decipher import PublicKeyManager
from google_payment_token_decipher.models.ecv2 import Ecv2
from google_payment_token_decipher.models.payment_method_token import PaymentMethodToken
from google_payment_token_decipher.models.signed_Key import SignedKey
from google_payment_token_decipher.utils import to_length_value


class PaymentTokenDecryption:
    """
    Convert a google payment token into a decryption payment token.

    """

    def __init__(
        self,
        keys: List[bytes],
        production: bool = False,
        refresh_background: bool = True,
    ):
        """
        Payment token decryption object used to decrypt a Google payment token payload

        Setting refresh_background to False can result in a false positive payment token validation,
        using it causes some delay for every request but insure security, use wisely
        :param production: Choose between production and test environment
        :param refresh_background: Activate Google certificate auto refresh for every request (most secure mode)
        """

        self.public_key_manager: PublicKeyManager = PublicKeyManager(
            production, refresh_background
        )
        self.keys = keys

    def decrypt(self, message: Union[dict, PaymentMethodToken]):
        """

        :return:
        """
        if isinstance(message, dict):
            message = PaymentMethodToken(**message)
        public_key_manager: Ecv2 = self.public_key_manager.keyset()
        self._verify_intermediate_signing_key(message, public_key_manager)
        self._verify_payload_signature(message, public_key_manager)
        decrypted_message = self._decrypt(message)
        return decrypted_message

    def _verify_intermediate_signing_key(self, message: PaymentMethodToken, public_key_manager: Ecv2):
        """
        google payload decryptor step 2
        Verify that the that signature of the intermediate signing key is valid
        """
        if not message.protocolVersion == public_key_manager.protocolVersion:
            raise Exception("change for custom one, but ecv1 not supported")

        key = ECC.import_key(public_key_manager.keyValue)
        # TODO add type inting for verifier
        verifier = DSS.new(key, 'fips-186-3', encoding='der')
        sha_content: bytearray = to_length_value(
            'Google',
            message.protocolVersion,
            message.intermediateSigningKey.signedKey
        )
        sha = SHA256.new(sha_content)

        # step 2 bis: verify that all signature veri
        for sig in message.intermediateSigningKey.signatures:
            verifier.verify(sha, base64.b64decode(sig))

        signed_key: SignedKey = SignedKey(**json.loads(message.intermediateSigningKey.signedKey))

        if int(signed_key.keyExpiration) - int(time.time()) * 1000 <= 3600:
            raise Exception("custom exception but key is too old (should have 1h left)")

    def _verify_payload_signature(self, message, public_key_manager: Ecv2):
        pass

    def _decrypt(self, message) -> bytes:
        keys = self.keys
        pass