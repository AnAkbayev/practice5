import re
import json
from pathlib import Path


def parse_receipt(filename="raw.txt"):
    text = Path(filename).read_text(encoding="utf-8")

    # Product lines have the form:
    # quantity x product name    price
    product_pattern = re.compile(
        r"^\s*(\d+)\s*x\s+(.+?)\s+([\d,]+\.\d{2})\s*$",
        re.MULTILINE,
    )

    products = []
    for match in product_pattern.finditer(text):
        quantity = int(match.group(1))
        name = match.group(2).strip()
        price = float(match.group(3).replace(",", ""))
        products.append({
            "quantity": quantity,
            "name": name,
            "price": price,
        })

    # Find monetary values at the end of receipt lines.
    # This avoids treating measurements such as 0.5L as prices.
    price_pattern = r"(?m)^.*?((?:\d{1,3}(?:,\d{3})+|\d+)\.\d{2})\s*$"
    prices = [
        float(match.replace(",", ""))
        for match in re.findall(price_pattern, text)
    ]

    # Date and time.
    date_time_match = re.search(
        r"Date:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
        text,
    )

    # Payment method.
    payment_match = re.search(r"Payment method:\s*(.+)", text)

    # Total amount.
    total_match = re.search(
        r"^TOTAL\s+([\d,]+\.\d{2})\s*$",
        text,
        re.MULTILINE,
    )

    result = {
        "products": products,
        "all_prices": prices,
        "total": float(total_match.group(1).replace(",", ""))
        if total_match else None,
        "date": date_time_match.group(1) if date_time_match else None,
        "time": date_time_match.group(2) if date_time_match else None,
        "payment_method": payment_match.group(1).strip()
        if payment_match else None,
    }

    return result


if __name__ == "__main__":
    data = parse_receipt()
    print(json.dumps(data, indent=4, ensure_ascii=False))
