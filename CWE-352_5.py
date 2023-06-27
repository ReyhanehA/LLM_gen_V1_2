#2.# Example 2: CWE-352 - Cross-Site Request Forgery (CSRF)

from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/transfer', methods=['POST'])
def transfer_funds():
    amount = request.form['amount']
    account_number = request.form['account_number']
    # Transfer funds to the specified account
    return redirect('/success')

# The vulnerable line is the request.form[] call, which can be manipulated by an attacker to transfer funds to a different account.