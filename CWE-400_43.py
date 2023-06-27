#4.# CWE-400: Uncontrolled Resource Consumption
# Vulnerable line: while len(data) > 0:
# Description: This code creates an infinite loop that consumes resources by checking the length of a string.
while len(data) > 0:
    pass