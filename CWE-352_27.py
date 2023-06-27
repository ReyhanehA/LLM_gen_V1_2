#4.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: <img src="http://attacker.com/steal_cookie.php">
# Description: The image tag is vulnerable to CSRF attacks as it allows an attacker to steal the user's session cookie and impersonate them on the website.