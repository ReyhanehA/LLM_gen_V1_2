#6.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = xml.etree.ElementTree.fromstring(request.data)
import xml.etree.ElementTree as ET
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = '<user><name>{}</name><age>{}</age></user>'.format(user.name, user.age)

response = requests.post('http://example.com', data=serialized_user)
data = ET.fromstring(response.content)