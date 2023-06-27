#1.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = pickle.loads(request.data)
import pickle
import requests

response = requests.get('http://example.com/data')
data = pickle.loads(response.content)