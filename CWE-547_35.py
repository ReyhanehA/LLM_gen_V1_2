#6.# CWE-547: Use of Deprecated Function
import os
os.system("echo 'Hello, World!'") # vulnerable line
# This code uses a deprecated function (os.system) which can be exploited by attackers to execute arbitrary commands.