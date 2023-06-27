#3.# Example 3: CWE-601 - Open Redirect

import urllib.parse
import urllib.request

def send_request():
    url = input("Enter a URL: ")
    data = urllib.parse.urlencode({'url': url}).encode()
    req = urllib.request.Request("https://example.com/redirect", data)
    response = urllib.request.urlopen(req)
    print(response.read())

# The vulnerable line is line 6 where the user input is directly passed to the urlencode function without validation.