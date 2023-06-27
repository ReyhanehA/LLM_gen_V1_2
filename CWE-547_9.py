#10.# CWE-547: Use of Hard-coded SMTP Credentials
# Vulnerable line: smtp.login("myemail@example.com", "mypassword")
email = input("Enter email address: ")
password = input("Enter email password: ")
smtp.login(email, password)