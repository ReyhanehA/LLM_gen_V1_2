#7.# CWE-502: Deserialization of Untrusted Data
# Vulnerable line: data = avro.schema.parse(request.data)
import avro.schema
import requests

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('John', 25)
serialized_user = '{"name": "User", "type": "record", "fields": [{"name": "name", "type": "string"}, {"name": "age", "type": "int"}]}'

response = requests.post('http://example.com', data=serialized_user)
data = avro.schema.parse(response.content)