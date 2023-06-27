#9.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = CAST.new(key, CAST.MODE_ECB)
# Description: Using the CAST algorithm in Electronic Codebook (ECB) mode is insecure and can lead to predictable ciphertext.
from Crypto.Cipher import CAST

key = b'secretkey'
plaintext = b'my secret message'

cipher = CAST.new(key, CAST.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)