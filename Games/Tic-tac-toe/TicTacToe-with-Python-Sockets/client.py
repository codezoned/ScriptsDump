import socket , pickle

HOST = '127.0.0.1'  
PORT = 80        
l=[333,333]
a = ([9,9,9],[9,9,9],[9,9,9])
def display(mat):
    for i in range(0,3):
        for j in range(0,3):
            if(mat[i][j]==9):
                a[i][j]='  '
            elif(mat[i][j]==1):
                a[i][j]='X'
            else:
                a[i][j]='O'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        data = s.recv(1024)
        txt=pickle.loads(data)
        if(txt=="Server wins" or txt=="Client wins"):
            print(txt)
            break
        data=pickle.loads(data)
        display(data)
        print(a[0])
        print(a[1])
        print(a[2])
        print("Enter your choice ")
        l[0]=input("Row ")
        l[1]=input("Column ")
        r , c = int(l[0]) , int(l[1])
        data[r][c]=0
        
        display(data)

        print(a[0])
        print(a[1])
        print(a[2])
        dl=pickle.dumps(l)
        s.send(dl)
    
