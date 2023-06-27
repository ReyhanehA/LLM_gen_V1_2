#1.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = pickle.loads(request.data)
import pickle
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = pickle.dumps(user)

response = requests.post('http://example.com', data=serialized_user)
data = pickle.loads(response.content)