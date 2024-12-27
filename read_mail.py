from flask import Flask, jsonify
from flask_cors import CORS
import imaplib
import email
from email.header import decode_header

app = Flask(__name__)
CORS(app)  # Enable CORS

# Email credentials (replace with your credentials or use environment variables)
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "enter-your-email@gmail.com"
EMAIL_PASSWORD = "Enter your password"

def fetch_emails():
    try:
        # Connect to the server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)

        # Login to your account
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

        # Select the mailbox you want to use (INBOX in this case)
        mail.select("inbox")

        # Search for all emails
        status, messages = mail.search(None, "ALL")

        # List to store email data
        emails = []

        # Convert messages to a list of email IDs
        email_ids = messages[0].split()

        for email_id in email_ids:
            # Fetch the email by ID
            res, msg = mail.fetch(email_id, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # Parse the raw email bytes
                    msg = email.message_from_bytes(response[1])
                    # Decode the email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # Decode bytes to string
                        subject = subject.decode(encoding if encoding else "utf-8")
                    # Decode email sender
                    from_ = msg.get("From")
                    # Decode the date
                    date = msg.get("Date")
                    # Extract the email body
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                break
                    else:
                        body = msg.get_payload(decode=True).decode()
                    
                    # Append the email data to the list
                    emails.append({
                        "id": email_id.decode(),
                        "from": from_,
                        "subject": subject,
                        "snippet": body[:100],  # Show the first 100 characters
                        "date": date
                    })

        # Close the connection and logout
        mail.close()
        mail.logout()

        return emails
    except Exception as e:
        print("Error fetching emails:", e)
        return []

@app.route('/get-emails', methods=['GET'])
def get_emails():
    emails = fetch_emails()
    return jsonify(emails)

if __name__ == '__main__':
    app.run(debug=True)
