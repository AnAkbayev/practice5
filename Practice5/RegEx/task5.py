import re

text = "Python starts this sentence."

match = re.match(r"Python", text)

print("Matched:", match.group() if match else "No match")
