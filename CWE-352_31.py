#8.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: <form action="/delete_account" method="POST"><input type="submit" value="Delete Account"></form>
# Description: The form is vulnerable to CSRF attacks as it allows an attacker to trick the user into submitting the form and deleting their account without their knowledge or consent.