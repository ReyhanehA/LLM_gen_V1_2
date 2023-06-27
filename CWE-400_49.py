#10.# CWE-400: Uncontrolled Resource Consumption
# Vulnerable line: while True:
# Description: This code creates an infinite loop that consumes resources by repeatedly creating subprocesses.
import subprocess
while True:
    subprocess.Popen(['ls'])