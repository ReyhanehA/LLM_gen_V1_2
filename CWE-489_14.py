#5.# CWE-489: Unreachable Code
# This code contains unreachable code that can be exploited by attackers
# Vulnerable line: line 7
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    print("This code is unreachable") # unreachable code