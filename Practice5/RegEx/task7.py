import re

text = "hello HELLO Hello"

print("Ignore case:", re.findall(r"hello", text, re.IGNORECASE))
