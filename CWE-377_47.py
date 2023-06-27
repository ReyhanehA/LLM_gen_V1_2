#8.# CWE-377: Insecure Session Management
# Vulnerable line: session_id = '12345'
# Description: This code uses a static session ID, which can be easily guessed or reused by an attacker to hijack a user's session.