#9.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = cloudpickle.loads(request.data)
import cloudpickle
import requests

response = requests.get('http://example.com/data')
data = cloudpickle.loads(response.content)