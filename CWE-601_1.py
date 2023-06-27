#3.# CWE-601: Open Redirect
# Vulnerable line: return HttpResponseRedirect(request.GET.get('next', '/'))
# Description: The code takes a redirect URL from the request parameters and redirects the user to that URL without proper validation. An attacker can craft a malicious URL to redirect the user to a phishing site or a malware download.