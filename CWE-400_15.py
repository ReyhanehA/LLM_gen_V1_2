#6.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large list of strings and joins them
# The vulnerability is that it does not limit the size of the list, which could lead to a memory exhaustion attack
strings = ['a' * 1000000 for i in range(100)]
result = ''.join(strings)