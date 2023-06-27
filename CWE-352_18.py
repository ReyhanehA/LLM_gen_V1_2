#5.# Example 5: CWE-352 - Cross-Site Request Forgery (CSRF)

import http.client

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        # Vulnerable line: CSRF token not checked
        conn = http.client.HTTPSConnection("example.com")
        conn.request("POST", "/change_password", body={'old_password': old_password, 'new_password': new_password})