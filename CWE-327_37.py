#8.# Example 8: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import bcrypt

password = "password123"
salt = bcrypt.gensalt(4)
hashed_password = bcrypt.hashpw(password.encode(), salt)
print(hashed_password) # Vulnerable line: using a weak salt for password hashing