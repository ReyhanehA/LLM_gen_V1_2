#9.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large list of sets and iterates over their elements
# The vulnerability is that it does not limit the size of the list, which could lead to a memory exhaustion attack
sets = [{i} for i in range(1000000)]
for s in sets:
    for element in s:
        pass