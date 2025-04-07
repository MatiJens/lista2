import pytest

from Zadanie1.Wielomian import Wielomian


def test_wielomian_init_valid():
    w = Wielomian([1, 2, 0, 0])
    assert w.wspolczynniki == [1, 2]
    assert w.stopienWielomianu() == 1

def test_wielomian_init_invalid():
    with pytest.raises(TypeError):
        Wielomian([1, "x", 3])

def test_wielomian_str():
    w = Wielomian([1,2,3])
    result = str(w)
    assert "W(x) = 3x^2 + 2x^1 + 1"

def test_wielomian_call():
    w = Wielomian([1, 2, 3])
    assert w(2) == 1 + 4 + 12

def test_wielomian_call_invalid():
    w = Wielomian([1, 2])
    with pytest.raises(TypeError):
        w("x")

def test_wielomian_add():
    w1 = Wielomian([1, 2])
    w2 = Wielomian([3, 0, 4])
    wynik = w1 + w2
    assert wynik.wspolczynniki == [4, 2, 4]

def test_wielomian_sub():
    w1 = Wielomian([5, 1])
    w2 = Wielomian([3, 0, 2])
    wynik = w1 - w2
    assert wynik.wspolczynniki == [2, 1, -2]

def test_wielomian_mul():
    w1 = Wielomian([1, 1])
    w2 = Wielomian([1, 1])
    wynik = w1 * w2
    assert wynik.wspolczynniki == [1, 2, 1]

def test_wielomian_add_typeerror():
    w = Wielomian([1])
    with pytest.raises(TypeError):
        _ = w + 5

def test_wielomian_sub_typeerror():
    w = Wielomian([1])
    with pytest.raises(TypeError):
        _ = w - 5

def test_wielomian_mul_typeerror():
    w = Wielomian([1])
    with pytest.raises(TypeError):
        _ = w * 5

def test_wielomian_iadd():
    w = Wielomian([1, 2])
    w += Wielomian([3])
    assert w.wspolczynniki == [4, 2]

def test_wielomian_isub():
    w = Wielomian([5, 1])
    w -= Wielomian([2, 1, 1])
    assert w.wspolczynniki == [3, 0, -1]

def test_wielomian_imul():
    w = Wielomian([1, 1])
    w *= Wielomian([1, 1])
    assert w.wspolczynniki == [1, 2, 1]

def test_wielomian_iadd_invalid_type():
    w = Wielomian([1])
    with pytest.raises(TypeError):
        w += 3

def test_wielomian_isub_invalid_type():
    w = Wielomian([1])
    with pytest.raises(TypeError):
        w -= 3

def test_wielomian_imul_invalid_type():
    w = Wielomian([1])
    with pytest.raises(TypeError):
        w *= 3