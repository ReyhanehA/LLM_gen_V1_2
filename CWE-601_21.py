#3.# CWE-601: URL Redirection to Untrusted Site
# Vulnerable line: redirect_url = input("Enter the redirect URL: ")
# Description: This code takes a redirect URL from user input without validating it, allowing an attacker to redirect the user to a malicious site.
redirect_url = input("Enter the redirect URL: ")