#4.# CWE-489: Unprotected Storage of Credentials
# This code stores credentials in an unprotected file that can be easily accessed by attackers
# Vulnerable line: line 5
import json

credentials = {"username": "admin", "password": "password123"}
with open("credentials.json", "w") as f:
    json.dump(credentials, f)