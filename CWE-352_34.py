#2.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: if request.method == 'POST':
# Description: The code is vulnerable to CSRF attacks as it does not verify the origin of the request, allowing an attacker to submit a request on behalf of the user without their knowledge or consent.
if request.method == 'POST':
  amount = request.POST.get('amount')
  to_account = request.POST.get('to_account')
  transfer_funds(amount, to_account)