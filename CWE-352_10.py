#7.# Example 7: CWE-352 - Cross-Site Request Forgery (CSRF)

import urllib.request

def update_profile(user_id, new_info):
    url = 'https://example.com/update_profile?id=' + user_id
    data = urllib.parse.urlencode(new_info).encode('utf-8')
    urllib.request.urlopen(url, data=data)

# The vulnerable line is the urllib.request.urlopen() call, which can be exploited by an attacker to update the user's profile with false information.