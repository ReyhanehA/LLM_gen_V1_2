#3.# CWE-547: Use of Insecure Random Number Generation
import random
secret_key = random.randint(1, 10) # vulnerable line
# This code uses an insecure random number generation method which can be easily predicted by attackers.