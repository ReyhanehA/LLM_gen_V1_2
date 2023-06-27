#2.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: if request.method == 'POST':
# Description: The code is vulnerable to CSRF attacks as it does not check the origin of the request, allowing an attacker to submit a forged request.