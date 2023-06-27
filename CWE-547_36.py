#7.# CWE-547: Use of Unprotected Storage
import pickle
data = {"username": "admin", "password": "password123"}
with open("data.pickle", "wb") as f:
    pickle.dump(data, f) # vulnerable line
# This code stores sensitive data (username and password) in an unprotected file (data.pickle) which can be easily accessed by attackers.