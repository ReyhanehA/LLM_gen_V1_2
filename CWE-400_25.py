#6.# CWE-400: Uncontrolled Resource Consumption
# This code creates an infinite loop with a sleep function, leading to potential denial of service attacks
import time

while True:
    time.sleep(1)