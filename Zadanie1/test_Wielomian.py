import pytest

from Zadanie1.Wielomian import Wielomian


def test_stopien_wielomianu():
    assert Wielomian([1,2,3]).stopienWielomianu() == 2
    assert Wielomian([1,2,3]).__str__() == "W(x) = 3x^2 + 2x^1 + 1"
    assert Wielomian([1,2,3])(3) == 34
    assert str(Wielomian([1,2,3]) + Wielomian([3,4,5,6])) == "W(x) = 6x^3 + 8x^2 + 6x^1 + 4"
    assert str(Wielomian([1,2,3]).__iadd__(Wielomian([3,4,5,6]))) == "W(x) = 6x^3 + 8x^2 + 6x^1 + 4"
    assert str(Wielomian([1,2,3]) - Wielomian([3,4,5,6])) == "W(x) = -6x^3 + -2x^2 + -2x^1 + -2"
    assert str(Wielomian([1,2,3]).__isub__(Wielomian([3,4,5,6]))) == "W(x) = -6x^3 + -2x^2 + -2x^1 + -2"
    assert str(Wielomian([1,2,3]) * Wielomian([3,4,5,6])) == "W(x) = 18x^5 + 27x^4 + 28x^3 + 22x^2 + 10x^1 + 3"
    assert str(Wielomian([1,2,3]).__imul__(Wielomian([3,4,5,6]))) == "W(x) = 18x^5 + 27x^4 + 28x^3 + 22x^2 + 10x^1 + 3"
    with pytest.raises(TypeError):
        Wielomian("[1,2,3]")
    with pytest.raises(TypeError):
        Wielomian([1,2,3])("3")