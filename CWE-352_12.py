#9.# Example 9: CWE-352 - Cross-Site Request Forgery (CSRF)

import urllib.request

def send_message(user_id, message):
    url = 'https://example.com/send_message?id=' + user_id
    data = urllib.parse.urlencode({'message': message}).encode('utf-8')
    urllib.request.urlopen(url, data=data)

# The vulnerable line is the urllib.request.urlopen() call, which can be exploited by an attacker to send a message to another user without the user's knowledge or consent.