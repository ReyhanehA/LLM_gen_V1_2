#3.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = yaml.load(request.data)
import yaml
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = yaml.dump(user.__dict__)

response = requests.post('http://example.com', data=serialized_user)
data = yaml.load(response.content)