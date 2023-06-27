#2.# CWE-489: Hardcoded Credentials
# This code contains hardcoded credentials that can be easily exploited by attackers
# Vulnerable line: line 4
import requests

username = "admin"
password = "password123"
url = "https://example.com/login"

response = requests.post(url, data={"username": username, "password": password})
print(response.text)