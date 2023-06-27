#2.# Example 2: CWE-352 - Cross-Site Request Forgery (CSRF)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/transfer', methods=['POST'])
def transfer_funds():
    amount = request.form['amount']
    recipient = request.form['recipient']
    # Vulnerable line: CSRF token not checked
    return render_template('transfer.html', amount=amount, recipient=recipient)