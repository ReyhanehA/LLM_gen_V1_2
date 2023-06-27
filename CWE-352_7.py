#4.# Example 4: CWE-352 - Cross-Site Request Forgery (CSRF)

import requests

def change_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        requests.post('https://example.com/change_password', data={'new_password': new_password})

# The vulnerable line is the requests.post() call, which can be exploited by an attacker to change the user's password without their knowledge or consent.