import re

text = "Python is easy to learn. Python is powerful."

match = re.search(r"Python", text)

print("Search result:", match.group() if match else "Not found")
