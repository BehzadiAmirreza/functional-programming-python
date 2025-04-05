from functools import partial

def send_email(sender, recipient, subject, message):
    print(f"From: {sender}")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Message: {message}", end="\n\n")

pfa_config = {
    "sender": "noreply@example.com", 
    "subject": "Daily Update"
}

update_for = partial(send_email, **pfa_config)
update_for(recipient="hey@andybek.com", message="hey there")
