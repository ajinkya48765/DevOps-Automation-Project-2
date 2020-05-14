import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host_address = "mymail@gmail.com"
host_pass = "mypass"
guest_address = "guest@gmail.com"
subject = "Report "
content = '''Test failed restart services'''

message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()

print('Successfully sent your mail')
