#9.# Insecure Cryptographic Storage:


import hashlib

password = input("Enter password: ")
hash = hashlib.md5(password.encode()).hexdigest()

# The vulnerable line is the use of the insecure MD5 hashing algorithm for password storage.