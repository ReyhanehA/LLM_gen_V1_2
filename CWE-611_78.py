#9.# CWE-611: Improper Input Validation
# Vulnerable line: line 5
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["testdb"]
collection_name = input("Enter a collection name: ")
db[collection_name].drop()