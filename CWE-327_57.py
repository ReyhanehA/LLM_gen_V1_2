#8.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = ARC2.new(key, ARC2.MODE_CFB, iv)
# Description: Using the ARC2 algorithm in Cipher Feedback (CFB) mode without proper initialization vector (IV) management can lead to predictable ciphertext.
from Crypto.Cipher import ARC2

key = b'secretkey'
iv = b'initialvec'
plaintext = b'my secret message'

cipher = ARC2.new(key, ARC2.MODE_CFB, iv)
ciphertext = cipher.encrypt(plaintext)