def rot13(word):
    #"rotate by 13 places" substitution cipher. Input: word that we want to code
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    for i in word:
        for j in alfabet:
            if i == j:
                if alfabet.index(j) > 13:
                    res.append( alfabet[alfabet.index(j)-13])
                else:
                    res.append( alfabet[alfabet.index(j)+13])
    return(res)
