#6.# Example 6: Use of input() function without proper input validation

user_input = input("Enter a password: ") # CWE-327: Use of input() function without proper input validation
if user_input == "password":
    print("Access granted")
else:
    print("Access denied")