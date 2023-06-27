#6.# Unrestricted File Upload:

# Vulnerable line:
file.save("/var/www/html/uploads/" + filename)

# Description: This code is vulnerable to unrestricted file upload as it allows an attacker to upload any file to the server without proper validation.