#10.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = dill.loads(request.data)
import dill
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = dill.dumps(user)

response = requests.post('http://example.com', data=serialized_user)
data = dill.loads(response.content)