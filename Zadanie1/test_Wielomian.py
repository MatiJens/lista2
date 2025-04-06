from Zadanie1.Wielomian import Wielomian


def test_stopien_wielomianu():
    w1 = Wielomian([1,2,3])
    w2 = Wielomian([3,4,5,6])
    assert w1.stopienWielomianu() == 2
    assert w1.__str__() == "W(x) = 3x^2 + 2x^1 + 1"
    assert w1(3) == 34
    assert w1 + w2 ==