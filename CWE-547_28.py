#9.# CWE-547: Use of Hard-coded Database Name
database_name = "mydatabase" # vulnerable line
# This code is vulnerable to CWE-547 as it uses a hard-coded database name which can be easily changed by attackers to point to a malicious database.