#3.# Example 3: CWE-352 - Cross-Site Request Forgery (CSRF)

import urllib.request

def delete_user(user_id):
    url = 'https://example.com/delete_user?id=' + user_id
    urllib.request.urlopen(url)

# The vulnerable line is the urllib.request.urlopen() call, which can be exploited by an attacker to delete a user without their knowledge or consent.