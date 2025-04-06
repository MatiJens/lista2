from Zadanie1.Wielomian import Wielomian

wielomianJeden = Wielomian([1,2,3])
wielomianDwa = Wielomian([3,4,5,6])
wielomianJedenSub = Wielomian([1,2,3])
wielomianDwaSub = Wielomian([3,4,5,6])
wielomianJedenMul = Wielomian([1,2,3])
wielomianDwaMul = Wielomian([3,4,5,6])

print(wielomianJeden.stopienWielomianu())
print(wielomianJeden)
print(wielomianJeden(3))

wielomianTrzy = wielomianDwa + wielomianJeden
wielomianCztery = wielomianJeden - wielomianDwa
wielomianPiec = wielomianDwa * wielomianJeden
wielomianJeden += wielomianDwa
wielomianJedenSub -= wielomianDwaSub
wielomianJedenMul *= wielomianDwaMul
print("dodawanie:")
print(wielomianTrzy)
print(wielomianJeden)
print("odejmowanie:")
print(wielomianCztery)
print(wielomianJedenSub)
print("mnozenie:")
print(wielomianPiec)
print(wielomianJedenMul)


