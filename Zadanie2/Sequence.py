from abc import ABC

class Sequence(ABC):
    """Reprezentuje sekwencję z unikalnym identyfikatorem i danymi.

    Abstrakcyjna klasa bazowa dla różnych typów sekwencji: DNA, RNA i białkowe.

    Atrybuty:
        identifier (str): Unikalny identyfikator sekwencji.
        data (list): Lista zawierająca elementy sekwencji.
        length (int): Długość sekwencji.
        VALID_CHARS (set): Zbiór dozwolonych znaków w sekwencji.
    """

    def __init__(self, identifier: str, data: list, VALID_CHARS: set):
        """Inicjalizuje obiekt Sequence z podanym identyfikatorem, danymi i dozwolonymi znakami.

        Args:
            identifier (str): Unikalny identyfikator sekwencji.
            data (list): Lista elementów sekwencji.
            VALID_CHARS (set): Zbiór dozwolonych znaków w sekwencji.
        """
        self.identifier = identifier
        self.data = data
        self.length = len(data)
        self.VALID_CHARS = VALID_CHARS

    def __str__(self):
        """Zwraca sformatowaną reprezentację tekstową sekwencji.

        Returns:
            str: Reprezentacja sekwencji w formacie FASTA.
        """
        return f"> {self.identifier}\n{''.join(self.data)}"

    def mutate(self, position: int, value: str):
        """Mutuje sekwencję, zastępując znak na określonej pozycji nowym znakiem.

        Args:
            position (int): Indeks pozycji w sekwencji do zmiany.
            value (str): Nowy znak do wstawienia na określonej pozycji.

        Raises:
            IndexError: Jeśli podana pozycja jest poza zakresem sekwencji.
            ValueError: Jeśli podany znak nie należy do dozwolonych znaków.
        """
        if (0 <= position < self.length):  # Sprawdza czy podana pozycja jest w granicach sekwencji
            if value in self.VALID_CHARS: # Sprawdza czy podany znak jest w zbiorze dozwolonych znaków
                self.data[position] = value  # Jeśli warunki są spełnione dokonuje mutacji zastępując znak na podanej pozycji
            else:
                raise ValueError(f"Znak '{value}' nie jest dozwolony.")
        else:
            raise IndexError("Pozycja poza zakresem sekwencji.")


    def findMotif(self, motif: list) -> list:
        """Wyszukuje wszystkie wystąpienia podanej sekwencji (motywu) w sekwencji głównej.

        Args:
            motif (list): Lista znaków reprezentujących szukany motyw.

        Returns:
            list: Lista indeksów początkowych, gdzie motyw został znaleziony.
        """
        motif_positions = []  # Inicjalizuje pustą listę na pozycje motywu
        motif_length = len(motif)  # Oblicza długość motywu
        for i in range(self.length - motif_length + 1): # Iteruje po sekwencji, uwzględniając długość motywu
            if self.data[i:i + motif_length] == motif: # Jeśli fragment sekwencji odpowiada motywowi
                motif_positions.append(i) # zapisuje początkowy indeks
        return motif_positions # Zwraca listę pozycji na których znaleziono motyw
