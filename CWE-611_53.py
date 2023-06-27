#4.# CWE-611: Improper Input Validation
# Vulnerable line: line 8
# Description: This code does not properly validate user input, allowing for potential buffer overflow attacks.
import ctypes

buffer = ctypes.create_string_buffer(10)
input_str = input("Enter a string: ")

ctypes.memmove(buffer, input_str, len(input_str))