#2.# CWE-489: Leftover Debug Code
# This code contains leftover debug code that can be exploited by attackers
# Vulnerable line: logging.debug("Debug info: %s", variable)
import logging
variable = "secret"
logging.debug("Debug info: %s", variable)