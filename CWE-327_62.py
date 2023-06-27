#3.# Example 3: Use of pickle module without proper input validation

import pickle

user_input = input("Enter a Python object: ")
serialized_obj = pickle.dumps(user_input)
deserialized_obj = pickle.loads(serialized_obj) # CWE-327: Use of pickle module without proper input validation
print("Deserialized object: ", deserialized_obj)