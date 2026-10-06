import re

text = "Age: 18, score: 95, year: 2026"

print("Digits:", re.findall(r"\d+", text))
print("Non-digits:", re.findall(r"\D+", text))
print("Word characters:", re.findall(r"\w+", text))
print("Whitespace:", re.findall(r"\s+", text))
