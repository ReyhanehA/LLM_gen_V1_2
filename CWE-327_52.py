#3.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
# Description: Using the Blowfish algorithm in Cipher Block Chaining (CBC) mode without proper initialization vector (IV) management can lead to predictable ciphertext.
from Crypto.Cipher import Blowfish

key = b'secretkey'
iv = b'initialvec'
plaintext = b'my secret message'

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
ciphertext = cipher.encrypt(plaintext)