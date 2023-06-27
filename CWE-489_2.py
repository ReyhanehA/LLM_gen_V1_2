#3.# CWE-489: Leftover Debug Code
# This code contains leftover debug code that can be exploited by attackers
# Vulnerable line: assert variable == expected_value, "Debug info: variable is not equal to expected_value"
variable = "secret"
expected_value = "password"
assert variable == expected_value, "Debug info: variable is not equal to expected_value"