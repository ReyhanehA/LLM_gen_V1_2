#9.# CWE-489: Unused Function Parameter
# This code contains an unused function parameter that can be exploited by attackers
# Vulnerable line: line 2
def get_user_info(user_id, user_name):
    user_info = {"id": user_id, "name": "John Doe", "email": "johndoe@example.com"}
    return user_info