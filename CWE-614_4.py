#5.# CWE-614: Use of Insufficiently Random Values
# Vulnerable line: session_id = random.randint(1, 100)
# Description: The session ID is being generated using a predictable random number generator, which can be easily guessed by attackers.