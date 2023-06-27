#6.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large file without checking its size, leading to potential disk space exhaustion
with open('output.txt', 'w') as f:
    f.write('a' * 100000000)