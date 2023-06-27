#4.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = xml.etree.ElementTree.fromstring(request.data)
import xml.etree.ElementTree as ET
import requests

response = requests.get('http://example.com/data')
data = ET.fromstring(response.content)