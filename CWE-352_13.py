#10.# Example 10: CWE-352 - Cross-Site Request Forgery (CSRF)

import requests

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        requests.post('https://example.com/create_post', data={'title': title, 'content': content})

# The vulnerable line is the requests.post() call, which can be exploited by an attacker to create a post on the user's behalf without their knowledge or consent.