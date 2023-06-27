#4.# CWE-400: Uncontrolled Resource Consumption
# This code creates an unbounded dictionary that can consume excessive memory
my_dict = {}
while True:
    my_dict['a'] = 'b'