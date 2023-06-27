#5.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: <form action="/change_password" method="POST">
# Description: The form action is vulnerable to CSRF attacks as it allows an attacker to change the user's password without their knowledge or consent.