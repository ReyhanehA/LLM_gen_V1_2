#3.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large list of numbers and sorts it
# The vulnerability is that it does not limit the size of the list, which could lead to a memory exhaustion attack
numbers = [i for i in range(1000000)]
numbers.sort()