#5.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = msgpack.unpackb(request.data)
import msgpack
import requests

response = requests.get('http://example.com/data')
data = msgpack.unpackb(response.content)