import string
import random

# main
def GeneratePassword(passLength):
    password = string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|}{[]"
    passwordList = []
    for passChar in range(passLength):
        passRandom = random.choice(password)
        passwordList.append(passRandom)
    finalOutput = "".join(passwordList)
    return finalOutput

if __name__ == "__main__":
    while True:
        try:
            userPasswordLength = int(input("Enter Length For Your Password: \n"))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        print(GeneratePassword(userPasswordLength))
        user_reply = input("Do You Want More? (y/n): ")
        if user_reply.lower() == "y":
            continue
        elif user_reply.lower() == "n":
            break
 