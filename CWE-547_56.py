#8.# Integer Overflow:


import sys

x = int(input("Enter number: "))
if x > sys.maxsize:
    print("Number too large")

# The vulnerable line is the lack of proper input validation, allowing for integer overflow attacks.