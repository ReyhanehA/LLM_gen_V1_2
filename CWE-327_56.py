#7.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = Salsa20.new(key=key, nonce=nonce)
# Description: Using the Salsa20 algorithm with a weak nonce can lead to predictable ciphertext and compromise the security of the communication.
from Crypto.Cipher import Salsa20

key = b'secretkey'
nonce = b'weaknonce'
plaintext = b'my secret message'

cipher = Salsa20.new(key=key, nonce=nonce)
ciphertext = cipher.encrypt(plaintext)