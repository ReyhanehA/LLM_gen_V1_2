#6.# Improper Input Validation:


import re

email = input("Enter email: ")
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email")
else:
    print("Invalid email")

# The vulnerable line is the lack of proper input validation, allowing for invalid input to be processed and potentially cause issues.