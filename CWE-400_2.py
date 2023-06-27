#3.# CWE-400: Uncontrolled Resource Consumption
# This code creates an unbounded list that can consume excessive memory
my_list = []
while True:
    my_list.append('a')