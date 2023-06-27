#9.# CWE-377: Insecure Database Queries
# Vulnerable line: cursor.execute('SELECT * FROM users WHERE username = ' + username)
# Description: This code concatenates user input into a database query, which can lead to SQL injection attacks.