#Sieve of Eratosthenes by Master-Fury

def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p=2                                       
    while (p * p <= n):
        if(prime[p]== True):
            for i in range (p*2,n+1,p):
                prime[i]= False
        p+=1
    for p in range (2,n):
        if prime[p]:
            print (p)

#DRIVER CODE
n=10                         #ENTER THE NUMBER HERE!!
print ("The following are the prime numbers smaller than or equal to ",n)
SieveOfEratosthenes(n)


##Description
##Given a number n, print all primes smaller than or equal to n.
##It is also given that n is a small number.
##The sieve of Eratosthenes is one of the most efficient ways to find all
##primes smaller than n when n is smaller than 10 million
##Time complexity : O(sqrt(n)loglog(n))
