#GCD of an Array Using Euclidean Algo By Master-Fury

def array_gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if(m%n)==0:
        return(n)
    else:
        return (gcd(n,m%n))

#DRIVER CODE

n= [2,4,6,8,16]               #Enter Your Numbers Here
result=array_gcd(n[0],n[1])
for i in range(2,len(n)):
    result=array_gcd(result,n[i])
print("GCD of given numbers is ",result)

##DESCRIPTION
##I have used Euclidean Algorithm to find GCD of two numbers which is a recursive method,
##also I have made this for an array of numbers.
##You can try also different methods like naive GCD and other.

    
