#Made By SHASHANK CHAKRAWARTY
"""
CONSIDER THE BELOW SATEMENT:
Let there be d digits in input integers.
Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers, for example, for decimal system, b is 10.
What is the value of d? If k is the maximum possible value, then d would be O(logb(k)).
So overall time complexity is O((n+b) * logb(k)).
"""


#here is your method for RADIX SORT
def radixsort(array):
  RADIX = 10
  maxLength = False
  temp , placement = -1, 1

  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for i in range( RADIX )]

    # split array between lists
    for i in array:
      temp = int((i / placement) % RADIX)
      buckets[temp].append(i)

 # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number

      if maxLength and temp > 0:
        maxLength = False

    # empty lists into lst array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        array[a] = i
        a += 1

    # move to next
    placement *= RADIX

#driver code you can change the values accordingly
array = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixsort(array)

print("Sorted elements are:")
for i in range(len(array)):
    
    print(array[i],end=' ')
