#9.# CWE-547: Use of Hard-coded SSH Key
# Vulnerable line: ssh_key = paramiko.RSAKey.from_private_key_file("/home/user/.ssh/id_rsa")
key_path = input("Enter SSH key path: ")
ssh_key = paramiko.RSAKey.from_private_key_file(key_path)