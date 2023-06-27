#10.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large list of lists and flattens it
# The vulnerability is that it does not limit the size of the list, which could lead to a memory exhaustion attack
lists = [[i] for i in range(1000000)]
result = [item for sublist in lists for item in sublist]