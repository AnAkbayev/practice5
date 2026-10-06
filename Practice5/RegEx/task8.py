import re

text = """first line
second line
third line"""

print("Lines starting with 's':",
      re.findall(r"^s.*$", text, re.MULTILINE))
