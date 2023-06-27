#6.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = ARC2.new(key, ARC2.MODE_CTR, counter=nonce)
# Description: Using the ARC2 algorithm in Counter (CTR) mode with a static nonce can lead to predictable ciphertext.
from Crypto.Cipher import ARC2

key = b'secretkey'
nonce = b'\x00\x01\x02\x03\x04\x05\x06\x07'
plaintext = b'my secret message'

cipher = ARC2.new(key, ARC2.MODE_CTR, counter=nonce)
ciphertext = cipher.encrypt(plaintext)