#10.# Cross-Site Request Forgery (CSRF):


from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    template = "<form method='POST' action='/transfer'><input type='hidden' name='amount' value='1000'><input type='submit' value='Transfer'></form>"
    return render_template_string(template)

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    # transfer money
    return 'Money transferred successfully!'

if __name__ == '__main__':
    app.run()


# The vulnerable line is line 7, where a form is rendered without a CSRF token, allowing for CSRF attacks where an attacker can trick a user into submitting the form without their knowledge.