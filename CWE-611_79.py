#10.# CWE-611: Improper Input Validation
# Vulnerable line: line 4
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import xml.etree.ElementTree as ET

xml_data = input("Enter XML data: ")
root = ET.fromstring(xml_data)