#10.# CWE-489: Uninitialized Variable
# This code contains an uninitialized variable that can be exploited by attackers
# Vulnerable line: line 4
def calculate_product(num_list):
    total = 1
    for num in num_list:
        total *= num
    print("The total is:", total)
    print("The product is:", product) # uninitialized variable