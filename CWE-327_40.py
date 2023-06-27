#1.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = DES.new(key, DES.MODE_ECB)
from Crypto.Cipher import DES