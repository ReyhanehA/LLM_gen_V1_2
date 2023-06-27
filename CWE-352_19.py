#6.# Example 6: CWE-352 - Cross-Site Request Forgery (CSRF)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_profile():
    name = request.form['name']
    email = request.form['email']
    # Vulnerable line: CSRF token not checked
    return render_template('profile.html', name=name, email=email)