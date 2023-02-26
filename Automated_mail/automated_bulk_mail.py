from email.message import EmailMessage
import ssl
import smtplib
import pandas as pd
import time
from datetime import date


class AutomatedMail():


    def __init__(self):
        welcome = "Welcome to Ajit Automated Mail service"
        print(welcome.center(125, '-'))


    def bulk_mail(self, file_name, column_name, sender_mail, sender_pass, subject, body):
        try:
            data = pd.read_csv(f"{file_name}.csv")
            mail = data.get(f"{column_name}")
            list_of_mail = list(mail)
            list_of_mail
        except Exception as e:
            print(e)
        try:
            sender = f"{sender_mail}"
            password = f"{sender_pass}"
            receiver = list_of_mail
            subject = f"{subject}"
            para = f"""
            {body}
            """
            em = EmailMessage()
            em['From'] = sender
            em['To'] = receiver
            em['Subject'] = subject
            em.set_content(para)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(sender, password)
                smtp.sendmail(sender, receiver, em.as_string())
            print("Your, Mail has been Send !!")
        except Exception as e:
            print("Error Occoured :-", e)


    def wait_3(self):
        i = 0
        while i < 3:
            print("----------------------------------------", end='')
            time.sleep(1)
            i = i + 1
        print('')

    def pass_instrustion(self):
        print("""
        Step 1. Go to Your 'Manage Your Google Account' | link:'https://myaccount.google.com/'\n
        Step 2. Then Go to 'Security' and activate your 2-Step Verification | link: 'https://myaccount.google.com/security'\n
        Step 3. After activating 2-Step Verification, search for App passwords or just see that after activation App password is just below 2-Step Verification\n
        Step 4. In App passwords in select app as option(others) then give a name to it (name does't matter)\n
        Step 5. Then generate your password\n
        Step 6. Use that 16-Digit password As-It-Is as password here\n
        After getting your 16-Digit password come back to mail, till then, Thank You
        """)


if __name__ == "__main__":
    mail = AutomatedMail()
    today = date.today()
    print(f"Date: {today}\n")
    print("Currently we only provide service to Gamil user's\n".center(125))
    mail.wait_3()
    print("Note:- Please copy your .csv file to same Directory\n".center(125))
    mail.wait_3()
    print("Make sure you have your 16-Digit Gmail password with you\n".center(125))
    mail.wait_3()
    print("Press 1 to get details how to get 16-Digit Google Gmail Password\n")
    print("Press 9 to contiune\n")
    ans = int(input("Enter:1/9\t"))
    if ans == 1:
        mail.wait_3()
        mail.pass_instrustion()
    elif ans == 9:
        file_name = input('Please enter the exact same name of your .csv file :\t')
        column_name = input("Please enter the exact same column name from file which contain Email's :\t")
        sender_mail = input("Enter the email id from your have to send mail :\t")
        sender_pass = input('Enter 16-Digit Password :\t')
        subject = input('Enter Subject Here :\t')
        body = input('Enter/Paste Hole Paragraph here :\t')
        mail.bulk_mail(file_name, column_name, sender_mail, sender_pass, subject, body)