#9.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = cloudpickle.loads(request.data)
import cloudpickle
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = cloudpickle.dumps(user)

response = requests.post('http://example.com', data=serialized_user)
data = cloudpickle.loads(response.content)