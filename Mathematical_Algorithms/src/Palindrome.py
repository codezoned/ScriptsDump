def palindrome(string):
    print(string)
    string = str(string)
    import math
    l = len(string)
    l2 = math.floor(l/2)
 
    first_half = string[ 0: l2]
    if l % 2 != 0:
        l2+=1
    second_half = string[l2: len(string)]
    second_half_rev = second_half[::-1]

    return(second_half_rev == first_half)
    
