import re

text = "Email us at student@example.com or admin@university.kz."

emails = re.findall(
    r"\b[\w.-]+@[\w.-]+\.[A-Za-z]{2,}\b",
    text
)

print("Emails:", emails)
