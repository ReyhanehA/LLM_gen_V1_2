#6.# CWE-489: Use of Externally-Controlled Format String
# This code uses an externally-controlled format string that can be exploited by attackers
# Vulnerable line: line 4
user_input = input("Enter your name: ")
print("Hello, %s!" % user_input)