#8.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = Salsa20.new(key=key, nonce=nonce)
# Description: Using the Salsa20 algorithm with a static nonce can lead to predictable ciphertext.
from Crypto.Cipher import Salsa20

key = b'secretkey'
nonce = b'\x00\x01\x02\x03\x04\x05\x06\x07'
plaintext = b'my secret message'

cipher = Salsa20.new(key=key, nonce=nonce)
ciphertext = cipher.encrypt(plaintext)