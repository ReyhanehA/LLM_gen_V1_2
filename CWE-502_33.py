#4.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = msgpack.unpackb(request.data)
import msgpack
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = msgpack.packb(user.__dict__)

response = requests.post('http://example.com', data=serialized_user)
data = msgpack.unpackb(response.content)