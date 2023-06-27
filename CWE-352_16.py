#3.# Example 3: CWE-352 - Cross-Site Request Forgery (CSRF)

import urllib.request

def delete_account(request):
    if request.method == 'POST':
        account_id = request.POST.get('account_id')
        # Vulnerable line: CSRF token not checked
        urllib.request.urlopen('https://example.com/delete_account?id=' + account_id)