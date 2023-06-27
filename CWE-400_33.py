#4.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large dictionary without checking its size, leading to potential memory exhaustion
my_dict = {i: i for i in range(100000000)}