#4.# Example 4: CWE-601 - Open Redirect

import requests

def send_request():
    url = input("Enter a URL: ")
    response = requests.get("https://example.com/redirect?url=" + url)
    print(response.content)

# The vulnerable line is line 5 where the user input is directly concatenated to the URL without validation.