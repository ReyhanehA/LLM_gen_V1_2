#9.# Example 9: Information Leakage

# Vulnerable line:
print("Invalid username or password.")

# Description: This code is vulnerable to information leakage because it provides too much information about why a login attempt failed, which could aid attackers in their attempts to gain access.