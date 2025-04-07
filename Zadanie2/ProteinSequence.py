from Zadanie2.Sequence import Sequence  # Import klasy bazowej Sequence

class ProteinSequence(Sequence):
    """
    Reprezentacja sekwencji Protein, dziedzicząca po klasie Sequence.

    Atrybuty:
        identifier (str): Identyfikator sekwencji Protein
        data (list): Sekwencja Protein
        length (int): Długość sekwencji
        VALID_CHARS (set): Dozwolone znaki w sekwencji DNA (aminokwasy)
    """

    def __init__(self, identifier: str, data: list,
                 VALID_CHARS={
                     "Ala", "Arg", "Asn", "Asp", "Cys",
                     "Glu", "Gln", "Gly", "His", "Ile",
                     "Leu", "Lys", "Met", "Phe", "Pro",
                     "Ser", "Thr", "Trp", "Tyr", "Val"
                 }):
        """
        Inicjalizuje obiekt ProteinSequence po sprawdzeniu poprawności nukleotydów.

        Args:
            identifier (str): Unikalny identyfikator sekwencji.
            data (list): Lista aminokwasow.
            VALID_CHARS (set): Dozwolone znaki w DNA (domyślnie aminokwasy).

        Raises:
            ValueError: Jeśli dane zawierają znaki spoza dozwolonego zbioru.
        """
        if all(aminokwas in VALID_CHARS for aminokwas in data):
            self.identifier = identifier
            self.data = data
            self.length = len(data)
            self.VALID_CHARS = VALID_CHARS
        else:
            raise ValueError("Niepoprawne nukleotydy wejsciowe")