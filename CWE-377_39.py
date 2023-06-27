#10.# CWE-377: Insecure Temporary File Creation

import tempfile

# Vulnerable line: creating a temporary file without setting secure permissions
temp_file = tempfile.gettempprefix()