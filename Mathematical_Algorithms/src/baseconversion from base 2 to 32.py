import datetime 
print("Today's Date and time is :", end=" ")
print(str(datetime.datetime.now()))
print("")
print("------This program converts number with any base to the base entered by the User with guaranteed accuracy of minimum 3 decimal places.------")
print("                        Note: base should be less than or equal to 32 and greater than equal to 2 ")
print("")
print("**It rounds off the number upto 20th decimal places**")
print("")
tsssy=""
while(tsssy==""):
  n=int(input("Enter base for the number"))
  print("")
  dic={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,'v':31}
  rttu=""   
  if n>10:
    xyzA=12
    while(xyzA>0):
      asd=[]
      akd=[]
      m=input("Enter Number with base "+str(n)).lower()
      print("")
      gg="".join(m)
      gg=gg.split(".")
      m=gg[0]
      xyz=0
      tty=0
      ks=0
      if len(gg)==2:
        for kjj in range(len(gg[1])):
          if 97<=ord(gg[1][kjj])<=122:
            u=gg[1][kjj]
            ks=dic[u]
            if int(ks)>=n:
              xyz=-1
            else:
              akd.append(str(ks))
          else:
            akd.append(gg[1][kjj])
          
        

      for i in range(len(m)):
        if 97<=ord(m[i])<=122:
          u=m[i]
          ks=dic[u]
          if int(ks)>=n:
            xyz=-1
          else:
            asd.append(str(ks))
        else:
          asd.append(m[i])
      if xyz==-1:
        xyzA=12
        print("Enter number again correctly, Make sure digits for the number should be less than the base of the number")
      else:
        xyzA=-9
   
  if n<=10:
    xyzA=12
    while(xyzA>0):
      asd=[]
      akd=[]
      m=input("Enter Number with base "+str(n)).lower()
      print("")
      gg="".join(m)
      gg=gg.split(".")
      m=gg[0]
      xyz=0
      ks=0
      if len(gg)==2:
        for kjj in range(len(gg[1])):
          ks=gg[1][kjj]
          if int(ks)>=n:
            xyz=-1
          
          else:
            akd.append(gg[1][kjj])
      for i in range(len(m)):
        if int(m[i])>=n:
          xyz=-1
        else:
          asd.append(m[i])
      if xyz==-1:
        xyzA=12
        print("Enter number again correctly, Make sure digits for the number should be less than the base of the number")
      else:
        xyzA=-9
  lm=int(input("Enter base to which you want to convert the given number"))
  print("")
  c=0
  d=0
  e=-1
  f=0
  t=1
  y=""
  if len(gg)==2:
    hj=1
    uu=1
  
    for ty in range(len(akd)):
      f+=int(akd[ty])*(n**e)
      e-=1
  
    while(hj<=20):
      uu=f*lm
    

      if int(uu)>=10:
        for i in range(97,119):
          if dic[chr(i)]==int(uu):
            rttu+=chr(i)
      if int(uu)<10:
        rttu+=str(int(uu))
      f=uu-int(uu)
      hj+=1  
        
    
  for i in range(len(asd)-1,-1,-1):
    c+=int(asd[i])*(n**d)
    d+=1
    
  while(t>0):
    ggg=c%lm
    if int(ggg)>=10:
      for iu in range(97,119):
        if dic[chr(iu)]==int(ggg):
          y+=chr(iu)
    if int(ggg)<10:
      y+=str(c%lm)
    c=c//lm
    if c==0:
      t=-1
  print("Number with base "+str(n)+" was "+".".join(gg)+" .Now it is converted into base "+str(lm)+" the required number is:",end=" ")
  print(y[::-1],end=".")
  if len(rttu)!=0:

    print(rttu)
  if len(rttu)==0:
    print(0)
  print("")
  uy=input("Press Enter to continue or hit any key to Exit !")



