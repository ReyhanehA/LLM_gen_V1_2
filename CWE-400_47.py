#8.# CWE-400: Uncontrolled Resource Consumption
# Vulnerable line: while True:
# Description: This code creates an infinite loop that consumes resources by repeatedly appending to a list.
my_list = []
while True:
    my_list.append('item')