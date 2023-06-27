#4.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = AES.new(key, AES.MODE_CFB, iv)
# Description: Using the AES algorithm in Cipher Feedback (CFB) mode with a static initialization vector (IV) can lead to predictable ciphertext.
from Crypto.Cipher import AES

key = b'secretkey'
iv = b'01234567'
plaintext = b'my secret message'

cipher = AES.new(key, AES.MODE_CFB, iv)
ciphertext = cipher.encrypt(plaintext)