#5.# CWE-489: Use of a Broken or Risky Cryptographic Algorithm
# This code uses a broken cryptographic algorithm that can be easily exploited by attackers
# Vulnerable line: line 4
import hashlib

password = "password123"
hash_object = hashlib.md5(password.encode())
print(hash_object.hexdigest())