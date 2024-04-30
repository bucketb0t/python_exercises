from exercitii_2 import div_3_5
import pytest


def test_div_3_5_caz_divizibil_3_5():
    assert div_3_5(15) == 35


def test_div_3_5_caz_divizibil_3():
    assert div_3_5(81) == 3


def test_div_3_5_caz_divizibil_5():
    assert div_3_5(100) == 5


@pytest.mark.parametrize("numar, expected", [
    (15, 35),
    (27, 3),
    (80, 5),
    (22, 5)])
def test_div_3_5(numar, expected):
    assert div_3_5(numar) == expected

    # Metoda normala la care se mai adauga situatia/cazurile pntru input_string, lista, nedivizibil cu 3 si/sau 5 si input boolean


def test_div_3_5_caz_nedivizibil_3_5():
    assert div_3_5(7) == "Nediviibil_3_5"

def test_div_3_5_caz_boolean():
    assert  div_3_5(True) == False
    assert div_3_5(False) == True

def test_div_3_5_caz_lista():
    assert div_3_5([1,"2",True]) == f"este lista: {[1,"2",True]}"


#ChatGPT
#
def test_div_3_5_caz_string(capfd):
    input_str = "12345"
    expected_output = '\n'.join(f"din str in caracter pe coloana {char}" for char in input_str)

    div_3_5(input_str)
    captured = capfd.readouterr().out.strip()

    assert captured == expected_output

