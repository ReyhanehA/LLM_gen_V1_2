#7.# CWE-547: Use of Hard-coded URL
url = "http://example.com/api" # vulnerable line
# This code is vulnerable to CWE-547 as it uses a hard-coded URL which can be easily changed by attackers to point to a malicious site.