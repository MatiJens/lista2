from itertools import zip_longest  # Import funkcji do łączenia list różnej długości z uzupełnieniem brakujących wartości

class Wielomian:
    def __init__(self, wspolczynniki : list):
        # Sprawdzenie, czy wszystkie elementy są liczbami (int lub float)
        if all(isinstance(a, (int, float)) for a in wspolczynniki):
            # Usunięcie zer z końca listy (niepotrzebne do zapisu wielomianu)
            while(wspolczynniki[-1] == 0):
                wspolczynniki.pop()
            # Zapisanie współczynników jako atrybutu obiektu
            self.wspolczynniki = wspolczynniki
        else:
            raise TypeError("Wspolczynniki powinny byc liczbami")  # Błąd, jeśli któryś współczynnik nie jest liczbą

    def stopienWielomianu(self):
        return (len(self.wspolczynniki) - 1)  # Zwraca stopień wielomianu (indeks ostatniego niezerowego współczynnika)

    def __str__(self):
        wzorWielomianu = "W(x) = "  # Początek tekstowej reprezentacji wielomianu
        n = (len(self.wspolczynniki) - 1)  # Najwyższy stopień
        for i in range(n):
            if(self.wspolczynniki[n-i] == 0):
                continue  # Pomijamy współczynniki zerowe
            else:
                wzorWielomianu += f"{self.wspolczynniki[n-i]}x^{n-i} + "  # Dodajemy kolejne wyrazy do wzoru
        wzorWielomianu += f"{self.wspolczynniki[0]}"  # Dodanie wyrazu wolnego (x⁰)
        return wzorWielomianu

    def __call__(self, x):
        wynik = 0  # Zmienna do przechowania wyniku
        if isinstance(x,(int,float)):
            n = (len(self.wspolczynniki) - 1)  # Najwyższy stopień
            for i in range(n):
                if (self.wspolczynniki[n - i] == 0):
                    continue  # Pomijamy wyrazy zerowe
                else:
                    wynik += self.wspolczynniki[n - i] * pow(x,(n-i))  # Dodajemy wartość danego wyrazu
            wynik += self.wspolczynniki[0]  # Dodajemy wyraz wolny
            return wynik
        else:
            raise TypeError("x musi być liczba")  # Obsługa błędu typu

    def __add__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            noweWspolczynniki = []
            # Łączenie współczynników tych samych stopni (z wypełnieniem zer)
            for i, j in zip_longest(wielomianNowy.wspolczynniki, self.wspolczynniki, fillvalue=0):
                noweWspolczynniki.append(i+j)
            return Wielomian(noweWspolczynniki)  # Zwrócenie nowego wielomianu
        else:
            raise TypeError("dodac mozna tylko wielomian z wielomianem")

    def __sub__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            noweWspolczynniki = []
            # Odejmowanie współczynników (z wypełnieniem zer)
            for i, j in zip_longest(wielomianNowy.wspolczynniki, self.wspolczynniki, fillvalue=0):
                noweWspolczynniki.append(j-i)
            return Wielomian(noweWspolczynniki)
        else:
            raise TypeError("odjac mozna tylko wielomian od wielomianu")

    def __mul__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            # Tworzymy listę zer do przechowania wynikowych współczynników
            noweWspolczynniki = [0] * (len(self.wspolczynniki) + len(wielomianNowy.wspolczynniki) - 1)
            # Mnożenie każdego składnika z każdym
            for i, a in enumerate(self.wspolczynniki):
                for j, b in enumerate(wielomianNowy.wspolczynniki):
                    noweWspolczynniki[i + j] += a * b
            return Wielomian(noweWspolczynniki)
        else:
            raise TypeError("pomnozyc mozna tylko wielomian z wielomianem")

    def __iadd__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            # Iteracja po współczynnikach dodawanego wielomianu
            for i in range(len(wielomianNowy.wspolczynniki)):
                if(len(self.wspolczynniki) > i):
                    self.wspolczynniki[i] += wielomianNowy.wspolczynniki[i]  # Odejmowanie, jeśli indeks istnieje
                else:
                    self.wspolczynniki.append(wielomianNowy.wspolczynniki[i]) # Dodanie współczynnika, jeśli za krótka lista
            return self
        else:
            raise TypeError("dodac mozna tylko wielomian z wielomianem")

    def __isub__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            # Iteracja po współczynnikach odejmowanego wielomianu
            for i in range(len(wielomianNowy.wspolczynniki)):
                if(len(self.wspolczynniki) > i):
                    self.wspolczynniki[i] -= wielomianNowy.wspolczynniki[i]  # Odejmowanie, jeśli indeks istnieje
                else:
                    self.wspolczynniki.append(-wielomianNowy.wspolczynniki[i])  # Dodanie współczynnika, jeśli za krótka lista
            return self
        else:
            raise TypeError("odjac mozna tylko wielomian od wielomianu")

    def __imul__(self, wielomianNowy):
        if isinstance(wielomianNowy,Wielomian):
            # Tworzymy listę wynikową na wynik mnożenia
            noweWspolczynniki = [0] * (len(self.wspolczynniki) + len(wielomianNowy.wspolczynniki) - 1)
            # Przeprowadzamy mnożenie wielomianów
            for i, a in enumerate(self.wspolczynniki):
                for j, b in enumerate(wielomianNowy.wspolczynniki):
                    noweWspolczynniki[i + j] += a * b
            self.wspolczynniki = noweWspolczynniki  # Nadpisujemy bieżące współczynniki
            return self
        else:
            raise TypeError("dodac mozna tylko wielomian z wielomianem")