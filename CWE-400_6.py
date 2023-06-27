#7.# CWE-400: Uncontrolled Resource Consumption
# This code creates an unbounded tuple that can consume excessive memory
my_tuple = ()
while True:
    my_tuple += ('a',)