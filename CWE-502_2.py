#3.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = yaml.load(request.data)
import yaml
import requests

response = requests.get('http://example.com/data')
data = yaml.load(response.content)