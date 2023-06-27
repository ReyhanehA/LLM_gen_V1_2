#7.# CWE-489: Unchecked Return Value
# This code contains an unchecked return value that can be exploited by attackers
# Vulnerable line: line 5
def read_file(filename):
    file = open(filename, "r")
    file_contents = file.read()
    file.close()
    return file_contents # unchecked return value