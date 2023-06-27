#8.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = pyarrow.deserialize(request.data)
import pyarrow
import requests

response = requests.get('http://example.com/data')
data = pyarrow.deserialize(response.content)