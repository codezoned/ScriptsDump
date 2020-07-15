#This is simple program to create a matrix.
from random import randint as r

while True:
    space, number =  r(0, 9), str(r(0, 9))
    print(space*" "+number+(space+2)*" "+number+(space+3)*" "+number)
