#3.# CWE-547: Use of Hard-coded Encryption Key
# Vulnerable line: cipher = AES.new(b"mysecretpassword", AES.MODE_CBC)
key = input("Enter encryption key: ")
cipher = AES.new(key.encode(), AES.MODE_CBC)