#10.# Information Leakage:

# Vulnerable line:
print("Invalid username or password")

# Description: This code is vulnerable to information leakage as it reveals to an attacker that the username or password is incorrect, potentially aiding in a brute-force attack.