import pytest
import Stack


def test_push():
    # Créer une pile de taille 2
    s = Stack.Stack(2)
    s.push(1)
    s.push(2)
    # Essayer d'ajouter un élément à une pile pleine
    with pytest.raises(IndexError):
        s.push(3)

def test_pop():
    # Créer une pile de taille 2
    s = Stack.Stack(2)
    # Essayer de supprimer un élément d'une pile vide
    with pytest.raises(IndexError):
        s.pop()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1
    # Essayer de supprimer un élément d'une pile vide
    with pytest.raises(IndexError):
        s.pop()

def test_isEmpty():
    # Créer une pile de taille 2
    s = Stack.Stack(2)
    assert s.isEmpty() == True
    s.push(1)
    assert s.isEmpty() == False

def test_isFull():
    # Créer une pile de taille 2
    s = Stack.Stack(2)
    assert s.isFull() == False
    s.push(1)
    s.push(2)
    assert s.isFull() == True