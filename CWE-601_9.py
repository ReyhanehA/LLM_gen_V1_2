#1.# Example 1: CWE-601 - Open Redirect

import flask
from flask import request, redirect

@app.route('/redirect')
def redirect_user():
    redirect_url = request.args.get('url')
    return redirect(redirect_url)

# The vulnerable line is line 6 where the redirect function is called without validating the input.