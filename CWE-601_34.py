#9.# Buffer Overflow:

# Vulnerable line:
buffer = bytearray(1024)
data = input("Enter data: ")
buffer[:len(data)] = data

# Description: This code is vulnerable to buffer overflow because it allows a user to input more data than the buffer can hold, potentially overwriting adjacent memory.