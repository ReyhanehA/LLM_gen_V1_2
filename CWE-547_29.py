#10.# CWE-547: Use of Hard-coded File Path
file_path = "/home/user/myfile.txt" # vulnerable line
# This code is vulnerable to CWE-547 as it uses a hard-coded file path which can be easily changed by attackers to access sensitive files.