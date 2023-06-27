#2.# CWE-377: Insecure Random Number Generation
# Vulnerable line: secret_key = random.randint(1, 100)
# Description: This code generates a random number using an insecure method, which can be easily predicted by an attacker.