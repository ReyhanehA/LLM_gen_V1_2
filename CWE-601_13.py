#5.# Example 5: CWE-601 - Open Redirect

import cgi

form = cgi.FieldStorage()

if "url" in form:
    url = form.getvalue("url")
    print("Location: " + url)
    print("Content-type: text/html\n")
    print("<html><head><title>Redirect</title></head><body>")
    print("<h1>Redirecting to " + url + "</h1>")
    print("</body></html>")

# The vulnerable line is line 4 where the user input is directly accessed without validation.