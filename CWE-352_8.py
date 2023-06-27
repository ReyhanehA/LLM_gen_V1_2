#5.# Example 5: CWE-352 - Cross-Site Request Forgery (CSRF)

import urllib.request

def add_friend(user_id):
    url = 'https://example.com/add_friend?id=' + user_id
    urllib.request.urlopen(url)

# The vulnerable line is the urllib.request.urlopen() call, which can be exploited by an attacker to add a friend to the user's account without their knowledge or consent.