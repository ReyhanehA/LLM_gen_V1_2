#2.# Cross-Site Scripting (XSS):


from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    template = "<h1>Hello, {{ name }}!</h1>"
    return render_template_string(template, name=name)

# The vulnerable line is the render_template_string function where user input is directly inserted into the HTML template, allowing for XSS attacks.