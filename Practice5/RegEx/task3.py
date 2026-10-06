import re

text = "apple,banana;orange|pear"

parts = re.split(r"[,;|]", text)

print("Split result:", parts)
