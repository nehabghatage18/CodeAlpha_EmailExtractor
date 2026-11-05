import re

# Read the input text file
with open("sample_emails.txt", "r") as file:
    text = file.read()

# Find email addresses using Regular Expressions
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern, text)

# Remove duplicate email addresses
emails = list(set(emails))

# Display extracted email addresses
print("===== EMAIL EXTRACTOR =====")
print("\nExtracted Email Addresses:\n")

for email in sorted(emails):
    print(email)

# Save extracted emails into an output file
with open("extracted_emails.txt", "w") as file:
    for email in sorted(emails):
        file.write(email + "\n")

print("\nEmail addresses saved successfully!")