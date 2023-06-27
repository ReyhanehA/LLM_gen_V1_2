#8.# Example 8: CWE-352 - Cross-Site Request Forgery (CSRF)

import requests

def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment = request.POST.get('comment')
        requests.post('https://example.com/add_comment', data={'post_id': post_id, 'comment': comment})

# The vulnerable line is the requests.post() call, which can be exploited by an attacker to add a comment to a post without the user's knowledge or consent.