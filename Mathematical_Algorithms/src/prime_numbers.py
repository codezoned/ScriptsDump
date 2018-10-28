

print("Type a number")
n = input()
a = 2
b = True #A boolean that tells us, if it is true so is a prime number, if not, is not a prime number


while a < int(n):#This will divide n to every natural number between 1 and n, a prime number wouldn't get a integer number 
	if int(n) % a == 0 :
		print("n is not a prime number!")
		a = int(n)#End this while
		b = False
		
	a = a + 1


	
if b == True:
	print("n is a prime number!")
