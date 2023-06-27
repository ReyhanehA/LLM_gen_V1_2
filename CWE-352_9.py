#6.# Example 6: CWE-352 - Cross-Site Request Forgery (CSRF)

import requests

def delete_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        requests.post('https://example.com/delete_post', data={'post_id': post_id})

# The vulnerable line is the requests.post() call, which can be exploited by an attacker to delete a post without the user's knowledge or consent.