from Zadanie2.ProteinSequence import ProteinSequence
from Zadanie2.Sequence import Sequence

class RNASequence(Sequence):
    """
    Reprezentacja sekwencji RNA, dziedzicząca po klasie Sequence.

    Atrybuty:
        identifier (str): Identyfikator sekwencji RNA.
        data (list): Sekwencja RNA
        length (int): Długość sekwencji
        VALID_CHARS (set): Dozwolone znaki w sekwencji DNA (A U C G)
    """

    def __init__(self, identifier: str, data: list, VALID_CHARS={"A", "U", "C", "G"}):
        """
        Inicjalizuje obiekt RNASequence po sprawdzeniu poprawności nukleotydów.

        Args:
            identifier (str): Unikalny identyfikator sekwencji.
            data (list): Lista nukleotydów.
            VALID_CHARS (set): Dozwolone znaki w DNA (domyślnie A, U, C, G).

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

    def translate(self, identifier: str):
        """
        Tłumaczy sekwencję RNA na sekwencję aminokwasową (białko).

        Tłumaczenie rozpoczyna się od kodonu startowego 'AUG',
        a kończy na pierwszym napotkanym kodonie stop ('UAA', 'UAG', 'UGA').

        Args:
            identifier (str): Identyfikator tworzonej sekwencji białkowej.

        Returns:
            ProteinSequence: Obiekt białka zawierający listę aminokwasów.
            str: Komunikat o braku kodonu start lub kodonu stop.
        """
        # w celu wykonania tego słownika wykorzystałem ChatGPT, prompt: "napisz mi slownik w pythonie kodon : aminokwas (wersja 3 literowa) pomin kodon start i stop"
        aminokwasy = {
            "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
            "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
            "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
            "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
            "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
            "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
            "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
            "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
            "UAU": "Tyr", "UAC": "Tyr", "CAU": "His", "CAC": "His",
            "CAA": "Gln", "CAG": "Gln", "AAU": "Asn", "AAC": "Asn",
            "AAA": "Lys", "AAG": "Lys", "GAU": "Asp", "GAC": "Asp",
            "GAA": "Glu", "GAG": "Glu", "UGU": "Cys", "UGC": "Cys",
            "UGG": "Trp", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
            "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
            "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
        }
        proteinData = [] # w tej liscie zapisywana jest struktura bialka - aminokwasy
        for i in range(len(self.data) - 2): # dla kazdego elementu (nukleotydu) w mRNA (zmniejszone o 2 poniewaz sprawdzamy dany element listy i dwa nastepne
            kodonStart = self.data[i] + self.data[i + 1] + self.data[i + 2] # zapisanie aktualnego elementu listy i dwoch nastepnym w formie zmiennej
            if kodonStart == "AUG": # jezeli ta zmienna jest rowna kodonowi startu przechodzimy do zapisywania bialka
                for j in range(i + 3, len(self.data) - 2, 3): # kolejna petla for, tym razem od wartosci (i + 3) pomijamy kodon startu do konca mRNA ze skokiem co 3 (z tylu kodonow sklada sie aminokwas)
                    kodon = self.data[j] + self.data[j + 1] + self.data[j + 2] # zapisanie aktualnego elementu listy i dwoch nastepnym w formie zmiennej
                    if kodon in aminokwasy: # jezeli ta zmienna jest ktorymkolwiek kluczem w slowniku aminokwasy
                        proteinData.append(aminokwasy[kodon]) # program dodaje wartosc dla tego klucza do listy bialka
                    if kodon in {"UAA", "UAG", "UGA"}: # jesli program natrafi na kodon stop
                        return ProteinSequence(identifier, proteinData) # konczy dzialanie funkcji i zwraca liste bialko
                return "brak kodonu stopu" # zwraca informacje ze nie w mRNA nie ma kodonu stop
        return "brak kodonu startu" # w przypadku gdy nie znajdzie sie kodon startu