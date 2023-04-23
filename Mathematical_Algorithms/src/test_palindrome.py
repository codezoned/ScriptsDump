import Palindrome
def test_String():
    assert Palindrome.palindrome("laval")==True      #chaine impaire
    assert Palindrome.palindrome("LAval")== True     # avec majuscule
    assert Palindrome.palindrome("Lav al") == True   # avec espace
    assert Palindrome.palindrome("Laval!!!") == True # avec ponctuation
    assert Palindrome.palindrome("deed")== True      #chaine paire
    assert Palindrome.palindrome("a") == True        # un seul caractere
    assert Palindrome.palindrome("") == False        #chaine vide
def test_otherType():
    assert Palindrome.palindrome(1221) == True         #nombre
    assert Palindrome.palindrome( 2 == 2 ) == True     #chaine contient nombre,symbole'=',espace
    assert Palindrome.palindrome(False) == False       #chaine mot clé
    assert Palindrome.palindrome([1, 'b', 1]) == False       #type Liste
    assert Palindrome.palindrome({'a':2, 'a':2}) == False    #type Dictionnaire

def test_With_Operator():
        assert Palindrome.palindrome("5+5")== True     #chaine contient nombre,operator +
        assert Palindrome.palindrome(5+5)== True       #meme chaine sans cotes
        assert Palindrome.palindrome(100-1)== False    #chaine avec operator -


