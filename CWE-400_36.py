#7.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large network packet without checking its size, leading to potential network congestion
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('example.com', 80))
s.sendall('a' * 100000000)