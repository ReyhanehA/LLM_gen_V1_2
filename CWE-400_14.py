#5.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large string and prints it
# The vulnerability is that it does not limit the size of the string, which could lead to a denial of service attack
s = 'a' * 1000000
print(s)