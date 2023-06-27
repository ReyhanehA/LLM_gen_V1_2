#1.# Example 1: CWE-352 - Cross-Site Request Forgery (CSRF)

import requests

def transfer_funds(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        account_number = request.POST.get('account_number')
        requests.post('https://bank.com/transfer', data={'amount': amount, 'account_number': account_number})

# The vulnerable line is the requests.post() call, which can be exploited by an attacker to transfer funds without the user's knowledge or consent.