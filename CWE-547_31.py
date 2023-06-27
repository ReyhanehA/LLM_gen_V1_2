#2.# CWE-547: Use of Weak Cryptographic Hash
import hashlib
password = "password123"
hash_object = hashlib.md5(password.encode())
print(hash_object.hexdigest()) # vulnerable line
# This code uses a weak cryptographic hash (MD5) which can be easily cracked by attackers.