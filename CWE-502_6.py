#7.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = avro.io.BinaryDecoder(request.data)
import avro.io
import requests

response = requests.get('http://example.com/data')
decoder = avro.io.BinaryDecoder(response.content)
data = decoder.read()