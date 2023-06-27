#7.# CWE-377: Insecure Cryptographic Algorithms
# Vulnerable line: hashed_password = hashlib.md5(password.encode()).hexdigest()
# Description: This code uses an insecure cryptographic algorithm (MD5) to hash a password, which can be easily cracked by an attacker.