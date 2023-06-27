#1.# Example 1: Use of eval() function without proper input validation

user_input = input("Enter a mathematical expression: ")
result = eval(user_input) # CWE-327: Use of eval() function without proper input validation
print("Result: ", result)