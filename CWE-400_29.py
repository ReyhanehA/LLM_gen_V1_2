#10.# CWE-400: Uncontrolled Resource Consumption
# This code creates an infinite loop with a file write operation, leading to potential denial of service attacks
while True:
    with open('output.txt', 'w') as f:
        f.write('Hello, world!')