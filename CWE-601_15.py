#7.# Example 7: CWE-601 - Open Redirect

import subprocess

def open_file():
    filename = input("Enter a filename: ")
    subprocess.call(["open", filename])

# The vulnerable line is line 4 where the user input is directly passed to the subprocess.call function without validation.