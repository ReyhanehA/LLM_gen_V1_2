#2.# Example 2: CWE-601 - Open Redirect

import webbrowser

def open_url():
    url = input("Enter a URL: ")
    webbrowser.open(url)

# The vulnerable line is line 4 where the user input is directly passed to the webbrowser.open function without validation.