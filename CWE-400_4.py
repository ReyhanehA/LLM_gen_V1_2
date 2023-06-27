#5.# CWE-400: Uncontrolled Resource Consumption
# This code creates an unbounded set that can consume excessive memory
my_set = set()
while True:
    my_set.add('a')