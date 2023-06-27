#10.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = IDEA.new(key, IDEA.MODE_OFB, iv)
# Description: Using the IDEA algorithm in Output Feedback (OFB) mode without proper initialization vector (IV) management can lead to predictable ciphertext.
from Crypto.Cipher import IDEA

key = b'secretkey'
iv = b'initialvec'
plaintext = b'my secret message'

cipher = IDEA.new(key, IDEA.MODE_OFB, iv)
ciphertext = cipher.encrypt(plaintext)