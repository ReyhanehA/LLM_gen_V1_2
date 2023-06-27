#6.# CWE-400: Uncontrolled Resource Consumption
# Vulnerable line: while True:
# Description: This code creates an infinite loop that consumes resources by repeatedly opening a file.
while True:
    file = open('file.txt', 'r')