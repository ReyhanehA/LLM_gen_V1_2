#9.# CWE-400: Uncontrolled Resource Consumption
# This code creates an unbounded recursion that can consume excessive memory
def my_function():
    my_function()