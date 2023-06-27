#9.# CWE-400: Uncontrolled Resource Consumption
# Vulnerable line: while True:
# Description: This code creates an infinite loop that consumes resources by repeatedly creating threads.
import threading
while True:
    t = threading.Thread(target=lambda: None)
    t.start()