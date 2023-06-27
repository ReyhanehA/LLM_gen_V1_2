#7.# Example 7: CWE-352 - Cross-Site Request Forgery (CSRF)

import urllib.request

def delete_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        # Vulnerable line: CSRF token not checked
        urllib.request.urlopen('https://example.com/delete_post?id=' + post_id)