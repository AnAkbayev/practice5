import re

text = "Dates: 06.10.2026, 25.12.2026, 01.01.2027"

dates = re.findall(
    r"\b\d{2}\.\d{2}\.\d{4}\b",
    text
)

print("Dates:", dates)
