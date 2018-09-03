# ARMSTRONG NUMBER BY SHASHANK

num=int(input('Enter a Number:'))
Sum=0
temp=num
while (temp > 0):
    digit=temp%10
    Sum+=digit**3
    temp//=10
   
    
if (num == Sum):
    print('Hurray! It is a Armstrong Number')
    
else:
    print('Sorry! Try again, Its not a Armstrong Number')



