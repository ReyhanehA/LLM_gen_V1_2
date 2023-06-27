#10.# Insufficient Input Validation:


import re

email = input("Enter email: ")

if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email.")
else:
    print("Invalid email.")

# The vulnerable line is the insufficient input validation, allowing for invalid email addresses to pass through and potentially cause issues downstream.