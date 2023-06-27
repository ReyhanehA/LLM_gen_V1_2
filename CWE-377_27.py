#8.# Example 8: CWE-377 - Insecure Cryptographic Algorithm

import hashlib

# Vulnerable line: using the MD5 cryptographic algorithm
password = "password123"
hashed_password = hashlib.md5(password.encode()).hexdigest()

# Description: This code uses the MD5 cryptographic algorithm, which is no longer considered secure and can be easily cracked by an attacker, leading to a potential security vulnerability.