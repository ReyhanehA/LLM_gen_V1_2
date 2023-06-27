#8.# CWE-400: Uncontrolled Resource Consumption
# This code creates an unbounded generator that can consume excessive memory
def my_generator():
    while True:
        yield 'a'