#10.# Example 10: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import cryptography.fernet

message = "Hello, world!"
key = cryptography.fernet.Fernet.generate_key()
f = cryptography.fernet.Fernet(key)
encrypted_message = f.encrypt(message.encode())
print(encrypted_message) # Vulnerable line: using a weak key for symmetric encryption