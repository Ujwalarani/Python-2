import re

# text = "python is good"
# if "python" in text:
#     print(text.find('python'))
#     print(text[0])
#
# index = text.find("good")
# if index != -1:
#     print (f"'good' found at index {index}")
#
# else:
#     print("pattern not found")

#text = "contact us at support@example.com"
text = "Due Dates: 10/06/2025, 15/06/2025"
#pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"
pattern = r"\b\d{2}/\d{2}/\d{4}"
dates = re.findall(pattern, text)
print("Dates found:", dates)

# match = re.search(pattern, text)
#
# if match:
#     print("Email found: ", match.group())

import re

def phone_number_search(text):

    """Search for phone numbers in the text."""

    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'


    matches = re.finditer(phone_pattern, text)

    for match in matches:

        print(f"Phone number found: {match.group()} at index {match.start()}")


if __name__ == "__main__":

   phone_text = "Call us at 123-456-7890 or 987.654.3210."

   print("\nPhone Number Search:")

phone_number_search(phone_text)

