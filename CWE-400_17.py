#8.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large list of dictionaries and iterates over their keys
# The vulnerability is that it does not limit the size of the list, which could lead to a memory exhaustion attack
dictionaries = [{i: i} for i in range(1000000)]
for d in dictionaries:
    for key in d:
        pass