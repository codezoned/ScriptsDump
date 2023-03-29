from Armstrong_Number import armstrongnumber

def test_armstrongnumber():
    assert armstrongnumber(153) == True
    assert armstrongnumber(371) == True
    assert armstrongnumber(65) == False
