#8.# CWE-489: Incomplete Control Flow
# This code contains incomplete control flow that can be exploited by attackers
# Vulnerable line: line 6
def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False
    print("This code is incomplete") # incomplete control flow