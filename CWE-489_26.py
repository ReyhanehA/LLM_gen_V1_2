#7.# CWE-489: Use of a Non-Constant Time Comparison Function
# This code uses a non-constant time comparison function that can be exploited by attackers
# Vulnerable line: line 5
import hmac

password = "password123"
key = "secret_key"
message = "login"
hash_object = hmac.new(key.encode(), message.encode(), "sha256")
if hash_object.digest() == password.encode():
    print("Login successful")
else:
    print("Login failed")