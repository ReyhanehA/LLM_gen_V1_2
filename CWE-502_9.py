#10.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = dill.loads(request.data)
import dill
import requests

response = requests.get('http://example.com/data')
data = dill.loads(response.content)