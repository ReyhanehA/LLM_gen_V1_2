#7.# Insecure Randomness:


import random

password = str(random.randint(1000, 9999))

# The vulnerable line is the use of the insecure random number generator, which can be easily predicted, allowing for password guessing attacks.