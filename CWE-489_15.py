#6.# CWE-489: Unused Variable
# This code contains an unused variable that can be exploited by attackers
# Vulnerable line: line 4
def get_user_email(user_id):
    user_info = {"id": user_id, "name": "John Doe", "email": "johndoe@example.com"}
    name = user_info["name"] # unused variable
    return user_info["email"]