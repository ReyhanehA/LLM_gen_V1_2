#6.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: if request.method == 'POST' and request.user.is_superuser:
# Description: The code is vulnerable to CSRF attacks as it does not verify the origin of the request, allowing an attacker to submit a request on behalf of the superuser without their knowledge or consent.
if request.method == 'POST' and request.user.is_superuser:
  delete_user(request.POST.get('user_id'))