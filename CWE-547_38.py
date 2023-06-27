#9.# CWE-547: Use of Unsanitized Input for Command Execution
import subprocess
command = input("Enter the command: ") # vulnerable line
subprocess.call(command, shell=True)
# This code uses unsanitized user input (command) for command execution, which can be exploited by attackers to execute arbitrary commands.