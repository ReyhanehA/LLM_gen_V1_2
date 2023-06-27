#6.# CWE-400: Uncontrolled Resource Consumption
# This code creates an unbounded string that can consume excessive memory
my_string = ''
while True:
    my_string += 'a'