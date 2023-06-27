#1.# CWE-400: Uncontrolled Resource Consumption
# This code reads an input file and copies its contents to an output file
# The vulnerability is that it does not limit the size of the input file, which could lead to a denial of service attack
with open('input.txt', 'r') as f:
    data = f.read()
with open('output.txt', 'w') as f:
    f.write(data)