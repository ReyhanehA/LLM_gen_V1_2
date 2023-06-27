#3.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large list without checking its size, leading to potential memory exhaustion
my_list = [i for i in range(100000000)]