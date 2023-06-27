#10.# CWE-377: Insecure Cross-Site Scripting (XSS)
# Vulnerable line: print('<script>alert("Hello, ' + name + '!");</script>')
# Description: This code outputs user input without sanitizing it, which can allow an attacker to inject malicious scripts into a web page.