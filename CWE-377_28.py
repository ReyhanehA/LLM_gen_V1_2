#9.# Example 9: CWE-377 - Insecure Cross-Site Scripting (XSS) Prevention

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Vulnerable line: using the unsafe render_template_string function
@app.route("/search")
def search():
    query = request.args.get("query")
    return render_template_string("<p>Search results for {{ query }}</p>", query=query)

# Description: This code uses the unsafe render_template_string function, which can allow an attacker to inject malicious code into the rendered HTML, leading to a potential security vulnerability.