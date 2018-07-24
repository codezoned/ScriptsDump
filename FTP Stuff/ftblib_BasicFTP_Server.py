"""
Written by Sagar Vakkala @ionicc

        FTP protocol (File Transfer Protocol) used to send and recieve files using a FTP server.

        This script is just for explanatory purpose and shouldn't be used on production.
        Even if used personally, Make sure to change the login username and id.

"""

from ftplib import FTP

ip = FTP('000.000.0.0')

ip.login(user='admin', passwd='pass')

ip.cwd('Enter path')


def getFile():
    file_name = 'something.txt'
    local_file = open(file_name, 'wb')
    ip.retrbinary(file_name, local_file.write, 1024)
    ip.quit()
    local_file.close()

def sendFile():
    file_name = 'something.txt'
    ip.storbinary('Got emm - ' + file_name, open(file_name, 'rb'))
    ip.quit()
