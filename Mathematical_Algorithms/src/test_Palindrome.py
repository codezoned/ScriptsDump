import Palindrome
def test_examples():
    assert Palindrome.palindrome("laval")==True
    assert Palindrome.palindrome("Laval")== False
    assert Palindrome.palindrome("deed")== True
    assert Palindrome.palindrome("100.001")== True
    assert Palindrome.palindrome("__main__"=="__niam") == True
    assert Palindrome.palindrome([1 ,'b', 1]) == False
    assert Palindrome.palindrome({2,2,2,2}) == False
    assert Palindrome.palindrome("a")== False
    assert Palindrome.palindrome("")== False
    assert Palindrome.palindrome(False)== False
def test_With_Operator():
        assert Palindrome.palindrome("5+5")== True
        assert Palindrome.palindrome(5+5)== True
        assert Palindrome.palindrome(100+1)== False

