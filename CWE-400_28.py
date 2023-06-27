#9.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large set without checking its size, leading to potential memory exhaustion
my_set = set(range(100000000))