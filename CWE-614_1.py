#2.# CWE-614: Sensitive Data in URL
# Vulnerable line: url = 'https://example.com/login?username=' + username + '&password=' + password
# Description: The username and password are being passed in the URL, which can be intercepted and viewed by attackers.