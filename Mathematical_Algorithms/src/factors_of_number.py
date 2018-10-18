#Author - @2hands10fingers
#Modified - @nishantcoder97 & @master-fury

def factors_of(number):
 return [i for i in range(1, number + 1) if number % i == 0]


#Driver Code
print(factors_of(6))
