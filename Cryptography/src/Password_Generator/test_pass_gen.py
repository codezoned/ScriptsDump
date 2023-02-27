import string
import random
import pass_gen
from pass_gen import GeneratePassword

def test_password_length():
    password = GeneratePassword(10)
    assert len(password) == 10, "wrong Password length "

def test_password_content():
    password = GeneratePassword(20)
    password_set = set(password)
    valid_set = set(string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|}{[]")
    assert password_set.issubset(valid_set), "Password should contain only letters, digits, and symbols."

def test_password_type():
    password = GeneratePassword(15)
    assert isinstance(password, str), "Password should be a string."

def user_reply(user_input):
    if user_input.lower() == "y":
        return True
    elif user_input.lower() == "n":
        return False
    else:
        return None

def test_user_reply():
    assert user_reply("y") == True, "user_reply should return True for 'y'."
    assert user_reply("n") == False, "user_reply should return False for 'n'."
    assert user_reply("x") == None, "user_reply should return None for other inputs."
    assert user_reply("") == None, "user_reply should return None for empty string."
    assert user_reply("yes") == None, "user_reply should return None for invalid input."

if __name__ == "__main__":
    test_password_length()
    test_password_content()
    test_password_type()
    test_user_reply()

    print("All tests passed successfully!")    
