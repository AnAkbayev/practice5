import re

text = "Prices: $12.50, $99.99, $1.25"

prices = re.findall(r"\$\d+(?:\.\d{2})?", text)

print("Prices:", prices)
