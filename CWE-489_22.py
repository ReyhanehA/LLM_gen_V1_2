#3.# CWE-489: Commented-Out Code
# This code contains commented-out code that can be exploited by attackers
# Vulnerable line: line 5
def calculate_sum(num_list):
    total = 0
    for num in num_list:
        total += num
    # print("The total is: ", total)
    return total