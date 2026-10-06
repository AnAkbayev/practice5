import re

text = "  Python   Regular Expressions  "

words = re.findall(r"\w+", text)
cleaned = " ".join(words)

print("Original:", repr(text))
print("Cleaned:", cleaned)
