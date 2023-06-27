#9.# Example 9: CWE-601 - Open Redirect

import webbrowser

def open_url():
    url = input("Enter a URL: ")
    webbrowser.open_new_tab(url)

# The vulnerable line is line 4 where the user input is directly passed to the open_new_tab function without validation.