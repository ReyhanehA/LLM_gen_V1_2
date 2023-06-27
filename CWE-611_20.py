#1.# Example 1: CWE-611 - Improper Restriction of XML External Entity Reference

import xml.etree.ElementTree as ET

xml_data = """
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<foo>&xxe;</foo>
"""

tree = ET.fromstring(xml_data)

# The vulnerable line is line 6 where the external entity reference is defined. This can allow an attacker to read sensitive files on the system.