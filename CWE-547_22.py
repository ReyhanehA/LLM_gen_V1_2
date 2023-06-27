#3.# CWE-547: Use of Hard-coded Encryption Key
encryption_key = "secretkey" # vulnerable line
# This code is vulnerable to CWE-547 as it uses a hard-coded encryption key which can be easily guessed or exploited by attackers.