#2.# CWE-489: Commented-Out Code
# This code contains commented-out code that can be exploited by attackers
# Vulnerable line: line 6
def calculate_average(num_list):
    total = 0
    for num in num_list:
        total += num
    # print("The total is:", total)
    # print("The length is:", len(num_list))
    # average = total / len(num_list)
    return average # commented-out code