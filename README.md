# SecureText 🔐

SecureText is a Python script that redacts sensitive information such as emails, phone numbers, and credit card numbers from a text file. It replaces them with `[REDACTED]` and also generates a summary log.

## Features
- Redacts:
  - Email addresses
  - Phone numbers
  - Credit card numbers
- Creates:
  - A redacted output file
  - A redaction summary log

## How to Use

1. Save your input text in a file named `input.txt`.
2. Run the script:

```bash
python secure_text.py
