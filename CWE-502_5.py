#6.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = bson.loads(request.data)
import bson
import requests

response = requests.get('http://example.com/data')
data = bson.loads(response.content)