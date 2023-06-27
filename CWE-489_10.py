#1.# CWE-489: Leftover Debug Code
# This code contains leftover debug code that can be exploited by attackers
# Vulnerable line: line 5
def calculate_sum(num_list):
    total = 0
    for num in num_list:
        total += num
    print("The total is:", total)
    print("DEBUG: num_list is", num_list) # leftover debug code