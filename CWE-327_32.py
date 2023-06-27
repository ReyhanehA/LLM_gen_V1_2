#3.# Example 3: CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

import hmac

message = "Hello, world!"
key = "secret_key"
hash_object = hmac.new(key.encode(), message.encode())
print(hash_object.hexdigest()) # Vulnerable line: using HMAC with a weak key