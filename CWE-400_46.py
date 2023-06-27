#7.# CWE-400: Uncontrolled Resource Consumption
# Vulnerable line: while True:
# Description: This code creates an infinite loop that consumes resources by repeatedly making network requests.
while True:
    response = requests.get('http://example.com')