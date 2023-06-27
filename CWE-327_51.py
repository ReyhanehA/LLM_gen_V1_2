#2.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = ARC4.new(key)
# Description: The ARC4 algorithm is vulnerable to key stream reuse attacks and should not be used for secure communication.
from Crypto.Cipher import ARC4

key = b'secretkey'
plaintext = b'my secret message'

cipher = ARC4.new(key)
ciphertext = cipher.encrypt(plaintext)