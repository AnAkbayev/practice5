import re

texts = [
    "cat",
    "cats",
    "cattt",
    "dog",
]

for text in texts:
    print(text, "->", bool(re.fullmatch(r"cat+", text)))
