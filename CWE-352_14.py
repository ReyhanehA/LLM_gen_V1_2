#1.# Example 1: CWE-352 - Cross-Site Request Forgery (CSRF)

import requests

def transfer_funds(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        recipient = request.POST.get('recipient')
        # Vulnerable line: CSRF token not checked
        requests.post('https://example.com/transfer', data={'amount': amount, 'recipient': recipient})