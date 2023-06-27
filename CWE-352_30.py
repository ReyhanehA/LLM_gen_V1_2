#7.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: <input type="hidden" name="csrf_token" value="123456">
# Description: The hidden input field is vulnerable to CSRF attacks as it allows an attacker to submit a forged request with a valid CSRF token.