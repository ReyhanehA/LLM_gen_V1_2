#7.# Example 7: CWE-377 - Insecure Session Management

from flask import Flask, session

app = Flask(__name__)
app.secret_key = "secret"

# Vulnerable line: using a predictable session ID
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "password123":
        session["user_id"] = 1
        return "Logged in successfully"
    else:
        return "Invalid credentials"

# Description: This code uses a predictable session ID, which can be easily guessed by an attacker, leading to a potential security vulnerability.