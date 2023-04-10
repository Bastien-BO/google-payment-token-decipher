from google_payment_token_decipher.payment_token_decryption import PaymentTokenDecipher

test = PaymentTokenDecipher()

caca = test.public_key_manager

print(caca.ecv2)
print(caca.__dict__)
