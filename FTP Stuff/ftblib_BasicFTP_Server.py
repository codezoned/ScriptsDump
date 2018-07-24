"""
Written by Sagar Vakkala @ionicc

        FTP protocol (File Transfer Protocol) used to send and recieve files using a FTP server.

        This script is just for explanatory purpose and shouldn't be used on production.
        Even if used personally, Make sure to change the login username and id.

"""
# Import the FTB module from the ftplib package

from ftplib import FTP

#Make a FTP server instance on your local ip

ip = FTP('000.000.0.0') #Replace this with your local ip

#Credentials to login to the server
ip.login(user='admin', passwd='pass') #This is completely opetion, But still if you use it. Change the username and password to something not that obvious

#The path used
ip.cwd('Enter path')


def getFile():
    file_name = 'something.txt'
    # wb = Write binary, rb = Read Binary
    local_file = open(file_name, 'wb')
    ip.retrbinary(file_name, local_file.write, 1024)
    ip.quit()
    local_file.close()

def sendFile():
    file_name = 'something.txt'
    ip.storbinary('Got emm - ' + file_name, open(file_name, 'rb'))
    ip.quit()
