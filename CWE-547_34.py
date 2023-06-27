#5.# CWE-547: Use of Unencrypted Communication
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("example.com", 80))
s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n") # vulnerable line
# This code sends data over an unencrypted communication channel, which can be intercepted and read by attackers.