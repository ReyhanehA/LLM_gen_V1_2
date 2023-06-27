#4.# CWE-489: Debug Information Leak
# This code contains debug information that can be leaked to attackers
# Vulnerable line: line 6
def get_user_info(user_id):
    user_info = {"id": user_id, "name": "John Doe", "email": "johndoe@example.com"}
    print("DEBUG: user_info is", user_info) # debug information leak
    return user_info