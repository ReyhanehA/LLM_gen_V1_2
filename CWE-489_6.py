#7.# CWE-489: Leftover Debug Code
# This code contains leftover debug code that can be exploited by attackers
# Vulnerable line: print("Debug info:", variable)
variable = "secret"
print("Debug info:", variable)