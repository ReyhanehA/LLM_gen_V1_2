#6.# Example 6: CWE-601 - Open Redirect

import os

def open_file():
    filename = input("Enter a filename: ")
    os.system("open " + filename)

# The vulnerable line is line 3 where the user input is directly concatenated to the "open" command without validation.