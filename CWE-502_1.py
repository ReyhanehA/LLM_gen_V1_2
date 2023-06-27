#2.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = json.loads(request.data)
import json
import requests

response = requests.get('http://example.com/data')
data = json.loads(response.content)