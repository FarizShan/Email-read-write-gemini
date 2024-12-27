from write_email import create_email
from send_email import send_email

final_email = create_email()
subject = input("Subject? \n")
recipient = input("To whom? \n")
cc=input("CC whom ?\n")

send_email(receiver_email=recipient, subject=subject, content=final_email, cc_emails=cc)
