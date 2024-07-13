import pandas as pd
import pywhatkit as kit
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send email
def send_email(to_email, name):
    from_email = "your_email@example.com"
    password = "your_email_password"

    # Create the email content
    subject = "Happy Birthday!"
    body = f"Dear {name},\n\nWishing you a very happy birthday!\n\nBest regards,\nYour Name"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Set up the server
    server = smtplib.SMTP('smtp.example.com', 587)  # Use your email provider's SMTP server and port
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Function to send WhatsApp message
def send_whatsapp_message(number, name):
    message = f"{name}!,confirmame si vamos a ir a la parrillada donde Vantroi el domingo 7 de julio please"
    kit.sendwhatmsg_instantly(f"+{number}", message, wait_time=5)

# Read the CSV file
df = pd.read_csv('birthdays.csv', dtype={'whatsapp_number': str})

# Get today's date
today = datetime.today().strftime('%Y-%m-%d')

# Loop through the CSV and send messages
for index, row in df.iterrows():
    if row['birthdate'] == today:
        send_whatsapp_message(row['whatsapp_number'], row['name'])
        send_email(row['email'], row['name'])

print("Messages sent successfully!")

