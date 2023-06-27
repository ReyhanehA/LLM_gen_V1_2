#5.# Example 5: CWE-377 - Insecure File Upload

from flask import Flask, request

app = Flask(__name__)

# Vulnerable line: allowing any file type to be uploaded
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file.save(file.filename)
    return "File uploaded successfully"

# Description: This code allows any file type to be uploaded, which can lead to a potential security vulnerability if an attacker is able to upload a malicious file.