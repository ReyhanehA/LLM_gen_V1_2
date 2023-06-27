#5.# Example 5: CWE-611 - Improper Restriction of XML External Entity Reference

import xml.etree.ElementTree as ET

xml_data = """
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "data:text/plain;base64,PHNjcmlwdD5hbGVydCgxMjM0KTwvc2NyaXB0Pg==" >]>
<foo>&xxe;</foo>
"""

tree = ET.fromstring(xml_data)

# The vulnerable line is line 6 where the external entity reference is defined. This can allow an attacker to execute arbitrary code in the context of the application.