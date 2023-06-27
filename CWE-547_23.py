#4.# CWE-547: Use of Hard-coded Credentials
username = "admin"
password = "password123" # vulnerable line
# This code is vulnerable to CWE-547 as it uses hard-coded credentials which can be easily guessed or exploited by attackers.