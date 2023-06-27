#10.# Example 10: Use of file I/O without proper input validation

filename = input("Enter a filename: ")
with open(filename, "r") as f: # CWE-327: Use of file I/O without proper input validation
    print(f.read())