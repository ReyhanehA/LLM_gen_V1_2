#10.# CWE-400: Uncontrolled Resource Consumption
# This code creates an unbounded loop that can consume excessive memory
i = 0
while i < float('inf'):
    i += 1