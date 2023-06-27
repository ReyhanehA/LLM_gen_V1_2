#2.# Example 2: CWE-377 - Insecure Random Number Generation

import random

# Vulnerable line: using the default random number generator
secret_key = str(random.getrandbits(128))

# Description: This code uses the default random number generator, which is not cryptographically secure and can be easily predicted by an attacker, leading to a potential security vulnerability.