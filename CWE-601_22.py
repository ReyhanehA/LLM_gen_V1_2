#4.# CWE-601: URL Redirection to Untrusted Site
# Vulnerable line: redirect_url = os.environ.get('REDIRECT_URL')
# Description: This code takes a redirect URL from an environment variable without validating it, allowing an attacker to redirect the user to a malicious site.
redirect_url = os.environ.get('REDIRECT_URL')