#1.# CWE-400: Uncontrolled Resource Consumption
# This code reads an input file without checking its size, leading to potential denial of service attacks
with open('input.txt', 'r') as f:
    data = f.read()