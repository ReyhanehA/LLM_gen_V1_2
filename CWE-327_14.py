#5.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = DES3.new(key, DES3.MODE_OFB, iv)
# Description: Using the Triple DES algorithm in Output Feedback (OFB) mode with a static initialization vector (IV) can lead to predictable ciphertext.
from Crypto.Cipher import DES3

key = b'secretkey'
iv = b'01234567'
plaintext = b'my secret message'

cipher = DES3.new(key, DES3.MODE_OFB, iv)
ciphertext = cipher.encrypt(plaintext)