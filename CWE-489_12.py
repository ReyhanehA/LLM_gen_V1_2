#3.# CWE-489: Hardcoded Password
# This code contains a hardcoded password that can be exploited by attackers
# Vulnerable line: line 4
def authenticate_user(username, password):
    if username == "admin" and password == "password123": # hardcoded password
        return True
    else:
        return False