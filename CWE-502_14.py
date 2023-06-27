#5.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = bson.loads(request.data)
import bson
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = bson.dumps(user.__dict__)

response = requests.post('http://example.com', data=serialized_user)
data = bson.loads(response.content)