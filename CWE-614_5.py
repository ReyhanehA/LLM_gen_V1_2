#6.# CWE-614: Use of Insecure Cryptographic Algorithm
# Vulnerable line: hashed_password = md5(password.encode()).hexdigest()
# Description: The MD5 algorithm is being used to hash the password, which is no longer considered secure.