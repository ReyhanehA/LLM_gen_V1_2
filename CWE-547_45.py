#6.# Insecure Cryptographic Storage:


import hashlib

password = input("Enter password: ")

hashed_password = hashlib.md5(password.encode()).hexdigest()

# The vulnerable line is the use of the insecure MD5 hashing algorithm, which can be easily cracked, allowing for password theft.