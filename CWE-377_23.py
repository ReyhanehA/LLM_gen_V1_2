#4.# Example 4: CWE-377 - Insecure Input Validation

import re

# Vulnerable line: using a regular expression without proper input validation
input_string = "Hello, world!"
if re.match("^Hello, [a-zA-Z]+!$", input_string):
    print("Valid input")
else:
    print("Invalid input")

# Description: This code uses a regular expression without proper input validation, which can lead to a potential security vulnerability if an attacker is able to inject malicious input.