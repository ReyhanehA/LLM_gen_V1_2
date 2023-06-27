#2.# Example 2: Use of exec() function without proper input validation

user_input = input("Enter a Python code: ")
exec(user_input) # CWE-327: Use of exec() function without proper input validation