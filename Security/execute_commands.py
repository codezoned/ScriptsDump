import subprocess
import smtplib
import os
import optparse
from optparse import OptionParser

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email, email, message)
    server.quit()

def main():
    parser = OptionParser()
    parser.add_option("-m", "--mail", dest="email", help="Your email")
    parser.add_option("-p", "--pass", dest="password", help="Your pass")
    (option, args) = parser.parse_args()
    email = option.email
    password = option.password
    while True:      
        try:
            print "\n"
            print("{0}~$: ".format(os.getcwd()))
            command = raw_input()
            result=subprocess.check_output(command, shell=True)
            send_mail(email,password, result)
        except KeyboardInterrupt:
            break
            print("Program complete.")

if __name__=='__main__':
    main()