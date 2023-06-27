#10.# CWE-352: Cross-Site Request Forgery (CSRF)
# Vulnerable line: <form action="/transfer_funds" method="POST"><input type="hidden" name="amount" value="100"><input type="submit" value="Transfer Funds"></form>
# Description: The form is vulnerable to CSRF attacks as it allows an attacker to trick the user into submitting the form and transferring funds without their knowledge or consent.