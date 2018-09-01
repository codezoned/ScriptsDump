#by: shashank
#armstrong number 

num=int(input('Enter a Number:'))
Sum=0
temp=num
while (temp > 0):
    digit=temp%10
    Sum+=digit**3
    temp//=10
   # print(digit,temp,Sum)
    
if (num == Sum):
    print('armstrong')
    
else:
    print('not armstrong')



