#5.# Unrestricted File Upload:


from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('/home/user/uploads/' + file.filename)

# The vulnerable line is the file.save function where user input is concatenated directly into the file path, allowing for unrestricted file upload attacks.