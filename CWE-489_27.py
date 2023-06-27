#8.# CWE-489: Use of a Potentially Dangerous Function
# This code uses a potentially dangerous function that can be exploited by attackers
# Vulnerable line: line 4
import os

filename = "file.txt"
os.system("rm " + filename)