#8.# CWE-547: Use of Hard-coded Port Number
port = 8080 # vulnerable line
# This code is vulnerable to CWE-547 as it uses a hard-coded port number which can be easily changed by attackers to point to a malicious service.