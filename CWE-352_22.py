#9.# Example 9: CWE-352 - Cross-Site Request Forgery (CSRF)

import http.client

def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment = request.POST.get('comment')
        # Vulnerable line: CSRF token not checked
        conn = http.client.HTTPSConnection("example.com")
        conn.request("POST", "/add_comment", body={'post_id': post_id, 'comment': comment})