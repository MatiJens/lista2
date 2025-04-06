from itertools import zip_longest


class Wielomian:
    def __init__(self, wspolczynniki : list):
        if all(isinstance(a, (int, float)) for a in wspolczynniki):
            while(wspolczynniki[-1] == 0):
                    wspolczynniki.pop()
            self.wspolczynniki = wspolczynniki
        else:
            raise TypeError("Wspolczynniki powinny byc liczbami")

    def stopienWielomianu(self):
        return (len(self.wspolczynniki) - 1)

    def __str__(self):
        wzorWielomianu = "W(x) = "
        n = (len(self.wspolczynniki) - 1)
        for i in range(n):
            if(self.wspolczynniki[n-i] == 0):
                continue
            else:
                wzorWielomianu += f"{self.wspolczynniki[n-i]}x^{n-i} + "
        wzorWielomianu += f"{self.wspolczynniki[0]}"
        return wzorWielomianu

    def __call__(self, x):
        wynik = 0
        if isinstance(x,(int,float)):
            n = (len(self.wspolczynniki) - 1)
            for i in range(n):
                if (self.wspolczynniki[n - i] == 0):
                    continue
                else:
                    wynik += self.wspolczynniki[n - i] * pow(x,(n-i))
            wynik += self.wspolczynniki[0]
            return wynik
        else:
            raise TypeError("x musi być liczba")

    def __add__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            noweWspolczynniki = []
            for i, j in zip_longest(wielomianNowy.wspolczynniki, self.wspolczynniki, fillvalue=0):
                noweWspolczynniki.append(i+j)
            return Wielomian(noweWspolczynniki)
        else:
            raise TypeError("dodac mozna tylko wielomian z wielomianem")

    def __sub__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            noweWspolczynniki = []
            for i, j in zip_longest(wielomianNowy.wspolczynniki, self.wspolczynniki, fillvalue=0):
                noweWspolczynniki.append(j-i)
            return Wielomian(noweWspolczynniki)
        else:
            raise TypeError("odjac mozna tylko wielomian od wielomianu")

    def __mul__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            noweWspolczynniki = []
            for i, j in zip_longest(wielomianNowy.wspolczynniki, self.wspolczynniki, fillvalue=0):
                noweWspolczynniki.append(i*j)
            return Wielomian(noweWspolczynniki)
        else:
            raise TypeError("pomnozyc mozna tylko wielomian z wielomianem")

    def __iadd__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            for i in range(len(wielomianNowy.wspolczynniki)):
                if(len(self.wspolczynniki) > i):
                    self.wspolczynniki[i] += wielomianNowy.wspolczynniki[i]
                else:
                    self.wspolczynniki.append(wielomianNowy.wspolczynniki[i])
            return self
        else:
            raise TypeError("dodac mozna tylko wielomian z wielomianem")

    def __isub__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            for i in range(len(wielomianNowy.wspolczynniki)):
                if(len(self.wspolczynniki) > i):
                    self.wspolczynniki[i] -= wielomianNowy.wspolczynniki[i]
                else:
                    self.wspolczynniki.append(-wielomianNowy.wspolczynniki[i])
            return self
        else:
            raise TypeError("odjac mozna tylko wielomian od wielomianu")

    def __imul__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            for i in range(len(wielomianNowy.wspolczynniki)):
                if(len(self.wspolczynniki) > i):
                    self.wspolczynniki[i] *= wielomianNowy.wspolczynniki[i]
                else:
                    break
            return self
        else:
            raise TypeError("pomnozyc mozna tylko wielomian z wielomianem")