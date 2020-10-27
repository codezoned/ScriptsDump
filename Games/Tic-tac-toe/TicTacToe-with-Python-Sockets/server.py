import socket , pickle
l=[333,333]
HOST ='127.0.0.1'
PORT = 80
arr = ([9,9,9],[9,9,9],[9,9,9])
a = ([9,9,9],[9,9,9],[9,9,9])

def check(mat):
    sum1=0
    sum2=0
    flag=0
    for i in range(0,3):
        for j in range(0,3):
            if(arr[i][j]=='x'):
                continue
            sum2=sum2+mat[i][j]
            if(i==j):
                sum1=sum1+mat[i][j]
        if(sum2==3 or sum2 == 0 and flag==1):
            return True
        else:
            sum2=0
    if(sum1==3):
        return True
    sum2=0
    for i in range(0,3):
        for j in range(0,3):
            if(arr[i][j]=='x'):
                continue
            sum2=sum2+mat[j][i]
            
        if(sum2==3 or sum2 == 0 and flag == 1):
            return True
        else:
            sum2=0
    flag=1

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
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    print(addr)
    with conn:
        print('Connected by', addr)
        while True:
            display(arr)
            print(a[0])
            print(a[1])
            print(a[2])
            if(check(arr)):
                print("Client Wins")
                txt="Clinet wins"
                txt=pickle.dumps(txt)
                conn.send(txt)
                break
            print("Enter your choice  ")
            l[0]=input("Row ")
            l[1]=input("Column ")
            x , y= int(l[0]) , int(l[1])
            arr[x][y]=1

            display(arr)

            print(a[0])
            print(a[1])
            print(a[2])
            if(check(arr)):
                print("Server wins")
                txt="Server wins"
                txt=pickle.dumps(txt)

                conn.send(txt)
                break
            
            
            data_string = pickle.dumps(arr)
            conn.send(data_string)
            data = conn.recv(1024)
            data = pickle.loads(data)
            r , c = int(data[0]) , int(data[1])
            arr[r][c]=0
            
           
