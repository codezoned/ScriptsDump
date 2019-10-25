"""
Bucket sort, or bin sort, is a sorting algorithm that works by distributing
the elements of an array into a number of buckets. Each bucket is then sorted
individually, either using a different sorting algorithm, or by recursively
applying the bucket sorting algorithm.

https://en.wikipedia.org/wiki/Bucket_sort

"""

from random import randint

def Bucket_Sort(A, Digit):
	B = [[] for x in range(10)]   #Creating 10 Buckets [10 different lists at every position]
	
	#Storing elements in Bucket according to their first digit
	for each in A: 
		B[int(str(each).rjust(Digit, '0')[0])].append(each)
	
	#Sorting Buckets
	for each in range(10):B[each].sort()
	
	A=[]
	
	#Assembling elements from all the buckets
	for bucket in B:
		for each in bucket:
			A.append(each)
	
	return A
	
A = [randint(0,99) for x in range(15)] #Generate a random list 

print("Orignal Array = ", A)

A = Bucket_Sort(A, 2)

print(" Sorted Array = ", A)
