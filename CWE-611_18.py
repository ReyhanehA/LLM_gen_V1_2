#9.# CWE-611: Improper Input Validation
# Vulnerable line: line 13
# Description: This code does not properly validate user input, allowing for potential cross-site scripting (XSS) attacks.
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()