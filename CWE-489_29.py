#10.# CWE-489: Use of Insufficiently Random Values
# This code uses insufficiently random values that can be easily guessed by attackers
# Vulnerable line: line 4
import random

password = "password" + str(random.randint(1, 100))
print(password)