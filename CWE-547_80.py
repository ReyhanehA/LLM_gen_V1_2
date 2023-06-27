#6.# Insecure Cryptographic Storage:


import hashlib

password = input("Enter password: ")
hash = hashlib.md5(password.encode()).hexdigest()
print("Hashed password: " + hash)


# The vulnerable line is line 3, where the MD5 algorithm is used for password hashing, which is vulnerable to brute-force attacks and rainbow table attacks.