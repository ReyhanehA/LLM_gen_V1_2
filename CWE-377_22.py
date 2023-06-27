#3.# Example 3: CWE-377 - Insecure Password Storage

import hashlib

# Vulnerable line: storing passwords in plain text
password = "password123"
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Description: This code stores passwords in plain text, which can be easily accessed by an attacker, leading to a potential security vulnerability.