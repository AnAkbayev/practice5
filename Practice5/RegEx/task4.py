import re

text = "My phone is 123-456-7890. Call 987-654-3210."

result = re.sub(r"\d{3}-\d{3}-\d{4}", "[PHONE]", text)

print(result)
