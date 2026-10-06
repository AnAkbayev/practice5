import re

text = "Name: Anzor, Age: 18, City: Almaty"

pattern = re.compile(
    r"Name:\s*(?P<name>[^,]+),\s*"
    r"Age:\s*(?P<age>\d+),\s*"
    r"City:\s*(?P<city>.+)"
)

match = pattern.search(text)

if match:
    print("Name:", match.group("name"))
    print("Age:", match.group("age"))
    print("City:", match.group("city"))
