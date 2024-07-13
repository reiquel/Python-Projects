import smtplib

my_email = "reiquel92@yahoo.com"
password = "Wfowhg6452$^*!@^$*^"  # Replace this with your app-specific password
friends_email = "carelary92@gmail.com"

connection = None  # Initialize connection to None

try:
    print("Connecting to the SMTP server...")
    connection = smtplib.SMTP("smtp.gmail.com", 587)  # Gmail SMTP server address
    connection.ehlo()
    print("Starting TLS...")
    connection.starttls()
    connection.ehlo()
    print("Logging in...")
    connection.login(user=my_email, password=password)
    print("Sending email...")
    connection.sendmail(
        from_addr=my_email,
        to_addrs=friends_email,
        msg="Subject:Hello\n\nHola mi amor, como estas?"
    )
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print(f"Failed to send email: Authentication error: {e}")
except smtplib.SMTPServerDisconnected as e:
    print(f"Failed to send email: Server disconnected unexpectedly: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if connection:
        try:
            print("Quitting the connection...")
            connection.quit()
        except smtplib.SMTPServerDisconnected:
            print("Connection already closed.")