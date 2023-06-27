#8.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = pyarrow.deserialize(request.data)
import pyarrow
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = pyarrow.serialize(user).to_buffer().to_pybytes()

response = requests.post('http://example.com', data=serialized_user)
data = pyarrow.deserialize(response.content)