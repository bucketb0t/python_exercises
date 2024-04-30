import pytest
from exercitii_3 import Product as Produs


# De bagat un handling pentru atunci cand se initializeaza produsul cu un dictionar sa se ridice o exceptie
# De folosit tipul de date try...

# Tema 2
# Get the type of the __init__ method
@pytest.mark.parametrize("nume, expected", [
    ("Test Name", "Test Name"),
    (27, "27"),
    (80.5, "80.5"),
    (True, "True"),
    (["Ana", "are", 3, "mere"], "Ana are 3 mere"),
    (None, "None"),
    # ({"key1": 1, "key2": 2, "key3": 3}, None)
])
def test_get_name(nume, expected):
    p = Produs(parametru_name=nume)
    assert p.get_name() == expected
    assert type(p.get_name()) == str


def test_get_name_exception():
    with pytest.raises(Exception, match="Inputul e dictionar"):
        p = Produs(parametru_name={"key1": 1, "key2": 2, "key3": 3})


def test_get_discount():
    p = Produs(parametru_discount=20)
    assert p.get_discount() == 20


def test_get_price():
    p = Produs(parametru_price=50)
    assert p.get_price() == 50


def test_get_category():
    p = Produs(parametru_category="TestCategory")
    assert p.get_category() == "TestCategory"


# De bagat parametrii pentru tipurile de cazuri facute insa sa se modifice functia cand intra data type diferite de string sa fie string

def test_set_name():
    p = Produs(parametru_name="OldName")
    new_name = "NewName"
    assert p.set_name(new_name) == new_name
    assert p.get_name() == new_name


def test_set_category():
    p = Produs(parametru_category="OldCategory")
    new_category = "NewCategory"
    assert p.set_category(new_category) == new_category
    assert p.get_category() == new_category


# Tema 2

def test_set_price():
    p = Produs(parametru_price=100)
    new_price = 90
    assert p.set_price(new_price) == new_price
    assert p.get_price() == new_price


def test_set_discount():
    p = Produs(parametru_discount=10)
    new_discount = 15
    assert p.set_discount(new_discount) == new_discount
    assert p.get_discount() == new_discount
