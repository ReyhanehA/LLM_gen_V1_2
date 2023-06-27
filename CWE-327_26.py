#7.# Example 7: Use of format() function without proper input validation

user_input = input("Enter your name: ")
print("Hello, {}".format(user_input)) # CWE-327: Use of format() function without proper input validation