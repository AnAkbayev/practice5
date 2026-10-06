import re

text = "username_123 user-name admin42"

usernames = re.findall(r"\b[A-Za-z_]\w*\b", text)

print("Valid username-like words:", usernames)
