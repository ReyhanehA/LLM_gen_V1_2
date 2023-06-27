#10.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = IDEA.new(key, IDEA.MODE_CFB, iv)
# Description: Using the IDEA algorithm in Cipher Feedback (CFB) mode with a static initialization vector (IV) can lead to predictable ciphertext.
from Crypto.Cipher import IDEA

key = b'secretkey'
iv = b'01234567'
plaintext = b'my secret message'

cipher = IDEA.new(key, IDEA.MODE_CFB, iv)
ciphertext = cipher.encrypt(plaintext)