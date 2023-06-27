#6.# CWE-611: Improper Input Validation
# Vulnerable line: line 5
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
hostname = input("Enter hostname: ")
ssh.connect(hostname, username='user', password='password')