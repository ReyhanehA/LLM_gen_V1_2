#8.# Broken Access Control:


from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/admin')
def admin():
    if not request.args.get('admin'):
        abort(403)
    return 'Welcome, admin!'

if __name__ == '__main__':
    app.run()


# The vulnerable line is line 7, where access control is not properly enforced and anyone can access the admin page by simply adding the 'admin' parameter to the URL.