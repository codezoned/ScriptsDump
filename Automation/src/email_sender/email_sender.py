import sys
import smtplib

# For different email option choose different server domain name
# for Gmail - smtp.gmail.com
# for Yahoo Mail - smtp.mail.yahoo.com
# for Outlook.com - smtp-mail.outlook.com

email = smtplib.SMTP("smtp.gmail.com", 587)  # for SSL encryption use port 465
email.ehlo()
email.starttls()  # skip this line if using SSL encryption
recipients = []
subject = input("Enter your Email's subject\n")
email_body = input("Enter your Email's body\n")
number_of_reciever = int(input("Enter number of receiver's\n"))
for i in range(number_of_reciever):
    recipients.append(input("reciever " + str(i + 1) + "'s email-id\n"))

my_email = input("Enter your email-id\n")
my_password = input("Enter you password\n")
try:
    email.login(my_email, my_password)
except:
    print(
        'Your email id or password is wrong \n google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure" so what you have to do is go to this link while you\'re logged in to your google account, and allow the access: https://www.google.com/settings/security/lesssecureapps \n'
    )
for i in range(number_of_reciever):
    email.sendmail(my_email, recipients[i], "Subject:" + subject + "\n" + email_body)
print("Your emails are sent :)")
email.quit()
