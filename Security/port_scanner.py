import optparse
import socket

def connScann(tgtHost, tgtPort):
    try:
        connSkt=socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        print "[+]%d/tcp open"% tgtPort
        connSkt.close()
    except:
        print '[-]%d\tcp closed'% tgtPort

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host {0}".format(tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan results for: '+tgtName[0]
    except:
         

def main():
    parser = optparse.OptionParser("usage%prog "+"-H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string',  help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='string',  help='specifict target port')
    (options, args) = parser.parse_args()
    tgtHost=options.tgtHost
    tgtPorts=str(options.tgtPort).split('. ')
    if tgtHost==None or tgtPorts==None:
        print("[-] Must specify target host and port(s)")
        exit()
    




if __name__ == '__main__':
    main()