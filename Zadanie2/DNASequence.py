from Zadanie2.RNASequence import RNASequence
from Zadanie2.Sequence import Sequence

class DNASequence(Sequence):
    """
    Reprezentacja sekwencji DNA, dziedzicząca po klasie Sequence.

    Atrybuty:
        identifier (str): Identyfikator sekwencji DNA.
        data (list): Sekwencja DNA
        length (int): Długość sekwencji
        VALID_CHARS (set): Dozwolone znaki w sekwencji DNA (A T C G)
    """

    def __init__(self, identifier: str, data: list, VALID_CHARS={"A", "T", "C", "G"}):
        """
        Inicjalizuje obiekt DNASequence po sprawdzeniu poprawności nukleotydów.

        Args:
            identifier (str): Unikalny identyfikator sekwencji.
            data (list): Lista nukleotydów.
            VALID_CHARS (set): Dozwolone znaki w DNA (domyślnie A, T, C, G).

        Raises:
            ValueError: Jeśli dane zawierają znaki spoza dozwolonego zbioru.
        """
        if all(nukleotyd in VALID_CHARS for nukleotyd in data):
            self.identifier = identifier
            self.data = data
            self.length = len(data)
            self.VALID_CHARS = VALID_CHARS
        else:
            raise ValueError("Niepoprawne nukleotydy wejsciowe")

    def complement(self):
        """
        Zwraca nić komplementarną do obecnej sekwencji DNA

        Returns:
            list: Odwrócona nić komplementarna DNA.
        """
        nic_matrycowa = []
        for i in range(len(self.data)):
            if self.data[i] == 'A':
                nic_matrycowa.insert(0, 'T')
            elif self.data[i] == 'T':
                nic_matrycowa.insert(0, 'A')
            elif self.data[i] == 'C':
                nic_matrycowa.insert(0, 'G')
            else:
                nic_matrycowa.insert(0, 'C')
        return nic_matrycowa

    def transcribe(self, identifier: str):
        """
        Transkrybuje sekwencję DNA do RNA (zamienia T na U)

        Args:
            identifier (str): Identyfikator nowej sekwencji RNA

        Returns:
            RNASequence: Obiekt klasy RNASequence reprezentujący przepisany łańcuch RNA
        """
        RNAData = []
        for nucleotide in self.data:
            if nucleotide == 'T':
                RNAData.append('U')
            else:
                RNAData.append(nucleotide)
        return RNASequence(identifier, RNAData)