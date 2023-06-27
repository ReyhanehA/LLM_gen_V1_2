#10.# CWE-547: Use of Unprotected Storage for Session Data
import flask
app = flask.Flask(__name__)
app.secret_key = "secret_key" # vulnerable line
# This code stores session data (secret_key) in an unprotected location (app.secret_key) which can be easily accessed by attackers.