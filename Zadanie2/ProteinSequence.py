from Zadanie2.Sequence import Sequence


class ProteinSequence(Sequence):

    def __init__(self, identifier: str, data: list,
                 VALID_CHARS={
                     "Ala", "Arg", "Asn", "Asp", "Cys",
                     "Glu", "Gln", "Gly", "His", "Ile",
                     "Leu", "Lys", "Met", "Phe", "Pro",
                     "Ser", "Thr", "Trp", "Tyr", "Val"
                 }):
        if all(aminokwas in VALID_CHARS for aminokwas in data):
            self.identifier = identifier
            self.data = data
            self.length = len(data)
            self.VALID_CHARS = VALID_CHARS
        else:
            raise ValueError("Niepoprawne nukleotydy wejsciowe")
