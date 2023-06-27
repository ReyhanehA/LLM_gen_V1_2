#9.# CWE-489: Improper Input Validation
# Vulnerable line: line 12
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import xml.etree.ElementTree as ET
xml_data = input("Enter some XML data: ")
root = ET.fromstring(xml_data)
print(root.tag)