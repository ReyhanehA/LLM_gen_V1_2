#2.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = json.loads(request.data)
import json
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = json.dumps(user.__dict__)

response = requests.post('http://example.com', data=serialized_user)
data = json.loads(response.content)