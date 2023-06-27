#6.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = ChaCha20.new(key=key, nonce=nonce)
# Description: Using the ChaCha20 algorithm with a weak nonce can lead to predictable ciphertext and compromise the security of the communication.
from Crypto.Cipher import ChaCha20

key = b'secretkey'
nonce = b'weaknonce'
plaintext = b'my secret message'

cipher = ChaCha20.new(key=key, nonce=nonce)
ciphertext = cipher.encrypt(plaintext)