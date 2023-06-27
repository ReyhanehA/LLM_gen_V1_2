#4.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = AES.new(key, AES.MODE_CFB, iv)
# Description: Using the AES algorithm in Cipher Feedback (CFB) mode without proper initialization vector (IV) management can lead to predictable ciphertext.
from Crypto.Cipher import AES

key = b'secretkey'
iv = b'initialvec'
plaintext = b'my secret message'

cipher = AES.new(key, AES.MODE_CFB, iv)
ciphertext = cipher.encrypt(plaintext)