import smtplib
import email.utils
from email.mime.text import MIMEText

# --- create our message ---
receiver_email = "ajeet.shakya@ekbana.info"
# receiver_email = "bibek.chaudhary@ekbana.info"
sender_email = "ramesh.rawal@ekbana.info"
password = "ekbana123"
subject = "Demo"
body = "Test message"
# Create our message.
msg = MIMEText('Testing email')
msg['To'] = email.utils.formataddr(('Ajeet Shakya', receiver_email))
msg['From'] = email.utils.formataddr(('Ramesh Rawal', sender_email))
msg['Subject'] = body

# --- send the email ---

# SMTP() is used with normal, unencrypted (non-SSL) email.
# To send email via an SSL connection, use SMTP_SSL().
server = smtplib.SMTP()

# Specifying an empty server.connect() statement defaults to ('localhost', 25).
# Therefore, we specify which mail server we wish to connect to.
server.connect ('mail.ekbana.info', 25)

# Optional login for the receiving mail_server.
# server.login (sender_email, password)

# Dump communication with the receiving server straight to to the console.
# server.set_debuglevel(True)

# 'yourname@yourdomain.com' is our envelope address and specifies the return
# path for bounced emails.
try:
    server.sendmail(sender_email, [receiver_email], msg.as_string())
finally:
    server.quit()