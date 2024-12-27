import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email,subject,content,cc_emails):
    sender_email = "your_email@gmail.com"
    receiver_email = receiver_email
    cc_emails = [cc_emails]
    password = "Enter your password"

    # Create the email content
    subject = subject
    body = content

    # Set up the MIME structure
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Cc"] = ", ".join(cc_emails)
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    all_recipients = [receiver_email] + cc_emails
    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            # server.sendmail(sender_email, receiver_email, message.as_string())
            server.sendmail(sender_email, all_recipients, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Run the function
if __name__ == "__main__":
    send_email()
