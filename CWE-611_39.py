#10.# CWE-611: Improper Input Validation
# Vulnerable line: line 13
# Description: This code takes user input without validating it, allowing for potential injection attacks.
import yaml
data = input("Enter some YAML data: ")
yaml_data = yaml.safe_load(data)
print(yaml_data)