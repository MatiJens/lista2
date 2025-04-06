from Zadanie2.RNASequence import RNASequence
from Zadanie2.Sequence import Sequence


class DNASequence(Sequence):

    def __init__(self, identifier : str, data : list, VALID_CHARS = {"A", "T", "C", "G"}):
        if all(nukleotyd in VALID_CHARS for nukleotyd in data):
            self.identifier = identifier
            self.data = data
            self.length = len(data)
            self.VALID_CHARS = VALID_CHARS
        else:
            raise ValueError("Niepoprawne nukleotydy wejsciowe")

    def complement(self):
        nic_matrycowa = []  # utworzenie pustej tablicy z wynikami
        for i in range(len(self.data)):  # sprawdzenie kazdego elementu listy wejsciowej i przypisanie do listy wyjsciowej odpowiedniej wartosci
            if self.data[i] == 'A':
                nic_matrycowa.insert(0, 'T')
            elif self.data[i] == 'T':
                nic_matrycowa.insert(0, 'A')
            elif self.data[i] == 'C':
                nic_matrycowa.insert(0, 'G')
            else:
                nic_matrycowa.insert(0, 'C')
        return nic_matrycowa

    def transcribe(self, identifier : str):
        RNAData = []
        for nucleotide in self.data:
            if nucleotide == 'T':
                RNAData += 'U'
            else:
                RNAData += nucleotide
        return RNASequence(identifier, RNAData)