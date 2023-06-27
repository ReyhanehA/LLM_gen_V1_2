#2.# CWE-400: Uncontrolled Resource Consumption
# Vulnerable line: for i in range(100000000):
# Description: This code creates a loop that iterates 100 million times, consuming resources.
for i in range(100000000):
    pass