import re

def redact_sensitive_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Patterns
    email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    credit_card_pattern = r'\d{4}[-\s]\d{1,6}[-\s]\d{1,5}[-\s]\d{1,5}|\d{4}[-\s]\d{6}[-\s]\d{1,5}'
    phone_pattern = r'(\+?\d{1,2}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}'
    
    def create_log_file():
        redaction_summary = {
            "Email": len(re.findall(email_pattern, content)),
            "Credit Card": len(re.findall(credit_card_pattern, content)),
            "Phone": len(re.findall(phone_pattern, content))
        }

        log_file = 'redaction_log.txt'
        with open(log_file, 'w', encoding='utf-8') as log:
            log.write("Redaction Summary:\n\n")
            total = 0
            for label, count in redaction_summary.items():
                log.write(f"{label}: {count} redaction(s)\n")
                total += count
            log.write(f"\nTotal redactions: {total}\n")
        print(f"Log file '{log_file}' has been written successfully.")

    def create_output_file():
        redacted = re.sub(email_pattern, '[REDACTED]', content)
        redacted = re.sub(credit_card_pattern, '[REDACTED]', redacted)
        redacted = re.sub(phone_pattern, '[REDACTED]', redacted)

        output_file = 'redacted_output.txt'
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(redacted)
        print(f"Output file '{output_file}' has been written successfully.")

    create_log_file()
    create_output_file()
    print("Redaction completed successfully.")

if __name__ == '__main__':
    redact_sensitive_data('input.txt')
