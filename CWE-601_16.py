#8.# Example 8: CWE-601 - Open Redirect

import os

def open_file():
    filename = input("Enter a filename: ")
    os.startfile(filename)

# The vulnerable line is line 4 where the user input is directly passed to the startfile function without validation.