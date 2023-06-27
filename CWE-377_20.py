#1.# Example 1: CWE-377 - Insecure Temporary File Creation

import tempfile

# Vulnerable line: creating a temporary file with default permissions
temp_file = tempfile.NamedTemporaryFile()

# Description: This code creates a temporary file with default permissions, which can be accessed by other users on the system, leading to a potential security vulnerability.