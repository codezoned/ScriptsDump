import string

def rot13(word):
     #"rotate by 13 places" substitution cipher. Input: word that we want to code
    alfabet=list(string.ascii_lowercase)
    res = ''
    for i in word:
        if i in alfabet:
            res+=(alfabet[(alfabet.index(i)-13)])
    return(res)
