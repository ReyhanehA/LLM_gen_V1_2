#10.# Example 10: CWE-352 - Cross-Site Request Forgery (CSRF)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form['item']
    quantity = request.form['quantity']
    # Vulnerable line: CSRF token not checked
    return render_template('cart.html', item=item, quantity=quantity)