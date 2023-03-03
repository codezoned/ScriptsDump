import ROT13 as rot13
import pytest
def test_input0():
    assert ''.join(rot13.rot13('oussama')) == "bhffnzn"

def test_input1():
  with pytest.raises(TypeError,match="'bool' object is not iterable"):
    rot13.rot13(True) 


def test_input2():
  with pytest.raises(TypeError,match="'int' object is not iterable"):
    rot13.rot13(123)


def test_input3():
  with pytest.raises(TypeError,match="'int' object is not iterable"):
    assert rot13.rot13(0x33Aff)


def test_input4():
  assert ''.join(rot13.rot13("A"*999)) == ""*999

def test_input5():
  with pytest.raises(TypeError,match="'float' object is not iterable"):
    rot13.rot13(0.23548)

def test_input6():
  assert ''.join(rot13.rot13("     ")) == "     "

def test_input7():
  assert ''.join(rot13.rot13("TEST MAJUS")) == "GRFG ZNWHF"

def test_input8():
  assert ''.join(rot13.rot13("12345")) == "12345"  

def test_input9():
  assert ''.join(rot13.rot13("abcdefg12345")) == "nopqrst12345"

def test_input10():
  assert ''.join(rot13.rot13("test symboles #_@5+-_&")) == "grfg flzobyrf #_@5+-_&"

def test_input11():
  assert ''.join(rot13.rot13("test all 123543AZERabcde&€#&#_&")) == "grfg nyy 123543NMREnopqr&€#&#_&"

def test_input12():
  assert ''.join(rot13.rot13("test letter n")) == "grfg yrggre a"
