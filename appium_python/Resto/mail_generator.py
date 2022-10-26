# Imports
import smtplib
import time

# Language
error_title = "ERROR"
send_error = "I'm waiting {idle} and I will try again."
send_error_mail = "Mail invalid"
send_error_char = "Invalid character"
send_error_connection_1_2 = "Connection problem..."
send_error_connection_2_2 = "Gmail server is down or internet connection is instabil."
login_browser = "Please log in via your web browser and then try again."
login_browser_info = "That browser and this software shood have same IP connection first time."

# Gmaild ID fro login
fromMail = "pytestsiscs@gmail.com"
fromPass = "ucmjsensucafunsc"

# Some configurations
mailDelay = 15
exceptionDelay = 180


# SEND MAILS
def send_mail(email, thisSubject="Just a subject",
              thisMessage="This is just a simple message..."):
    # To ho to send mails
    mailTo = [
        email
    ]
    # If still have mails to send
    while len(mailTo) != 0:
        sendItTo = mailTo[0]  # Memorise what mail will be send it (debug purpose)
        try:
            # Connect to the server
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()

            # Sign In
            server.login(fromMail, fromPass)

            # Set the message
            message = f"Subject: {thisSubject}\n{thisMessage}"

            # Send one mail
            server.sendmail(fromMail, mailTo.pop(0), message)

            # Sign Out
            server.quit()

        # If is a problem
        except Exception as e:
            # Convert error in a string for som checks
            e = str(e)

            # Show me if...
            if "The recipient address" in e and "is not a valid" in e:
                print(f"\n>>> {send_error_mail} [//> {sendItTo}\n")
            elif "'ascii'" in e and "code can't encode characters" in e:
                print(f"\n>>> {send_error_char} [//> {sendItTo}\n")
            elif "Please" in e and "log in via your web browser" in e:
                print(f"\n>>> {login_browser}\n>>>  - {login_browser_info}")
                break
            elif "[WinError 10060]" in e:
                if "{idle}" in send_error:
                    se = send_error.split("{idle}");
                    seMsg = f"{se[0]}{exceptionDelay} sec.{se[1]}"
                else:
                    seMsg = send_error
                print(f"\n>>> {send_error_connection_1_2}\n>>> {send_error_connection_2_2}")
                print(f">>> {seMsg}\n")
                # Wait 5 minutes
                waitTime = exceptionDelay - mailDelay
                if waitTime <= 0:
                    waitTime = exceptionDelay
                time.sleep(waitTime)
            else:
                if "{idle}" in send_error:
                    se = send_error.split("{idle}");
                    seMsg = f"{se[0]}{exceptionDelay} sec.{se[1]}"
                else:
                    seMsg = send_error
                print(f">>> {error_title} <<<", e)
                print(f">>> {seMsg}\n")
                # Wait 5 minutes
                time.sleep(exceptionDelay)

        # If are still mails wait before to send another one
        if len(mailTo) != 0:
            time.sleep(mailDelay)