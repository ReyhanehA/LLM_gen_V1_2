#10.# Insufficient Authentication:


from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        session['logged_in'] = True
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('index'))

@app.route('/admin')
def admin():
    if session.get('logged_in'):
        return "Welcome, admin!"
    else:
        return redirect(url_for('index'))

# The vulnerable line is the lack of proper authentication checks, allowing for unauthorized access to the admin page.