import re

text = "cat, dog, bird, cat, fish"

animals = re.findall(r"\b\w+\b", text)

print("All words:", animals)
print("Cats:", re.findall(r"\bcat\b", text))
