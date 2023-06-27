#4.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large dictionary and iterates over its keys
# The vulnerability is that it does not limit the size of the dictionary, which could lead to a memory exhaustion attack
d = {i: i for i in range(1000000)}
for key in d:
    pass