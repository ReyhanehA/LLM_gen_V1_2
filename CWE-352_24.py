#1.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: form action="/transfer_funds" method="POST"
# Description: The form action is vulnerable to CSRF attacks as it allows an attacker to submit a form on behalf of the user without their knowledge or consent.