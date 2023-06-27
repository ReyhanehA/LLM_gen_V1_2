#4.# CWE-400: Uncontrolled Resource Consumption
# This code creates an infinite recursion, leading to potential stack overflow attacks
def recursive_function():
    recursive_function()