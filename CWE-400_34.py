#5.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large string without checking its size, leading to potential memory exhaustion
my_string = 'a' * 100000000