#importing libraries
import string
import random

#main
def GeneratePassword (passLength):
    password = string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
    ''' Generating characters, numbers and letters for password
        Use the string constant string.ascii_letters to get all the  lower and upper case letters.
    '''
    passwordList = []
    #password list is for putting all the selected password units into a string and show them to user
    for passChar in range(passLength):
        passRandom = random.choice(password) #The random.choice() function is used to choose a single item from any sequence.
        passwordList.append(passRandom) # appends the randomly picked character from password. 

    finalOutput = "".join(passwordList) # if password length == user's desired poass length returns password. 
    return finalOutput

import CreatePasswords as MyPassword

while 1:
    userPasswordLength = int(input("Enter Length For Your Password: \n"))
    print(MyPassword.GeneratePassword(userPasswordLength))
    userReply = input("Do You Want More? (y,n): ")
    if userReply.lower() == "y" :
        continue
    elif userReply.lower() == "n":
        break
