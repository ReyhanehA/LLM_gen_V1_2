#8.# CWE-400: Uncontrolled Resource Consumption
# This code creates an infinite loop with a print statement, leading to potential denial of service attacks
while True:
    print('Hello, world!')