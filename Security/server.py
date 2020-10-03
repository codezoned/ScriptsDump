import socket
import sys
import os

# Rules are as follows;

# Create socket object/ bind(host,port) / send / listen / recv / close

def build_socket():
    try:
        global host
        global port
        global sk

        host = ""
        port = 9999 
        sk = socket.socket()
    except:
        print("Error")

def bind_socket():
    try:
        global host
        global port
        global sk

        print("Binding Port ... " + str(port))
        sk.bind((host,port)) #Takes tuple of host/port as argument 
        sk.listen(5) #Listening will allow the server to look out for the connection

    except:
        print("Error")
        # Recursively call it until the bind is successful
        bind_socket()


def accept():
    global sk
    conn, address = sk.accept()
    if(conn != None):
        print("Connection has been accepted" + " IP Address: ", address[0], " Port#: ",address[1])
    read_cmd(conn)
    conn.close()

def read_cmd(conn):
    while True:
        cmd = input()
        if cmd == 'quit' or cmd == 'Quit':
            conn.close()
            sk.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            rcv = str(conn.recv(1024),"utf-8")
            print(rcv)
            print("\n")


def main():
    build_socket()
    bind_socket()
    accept()

main()
