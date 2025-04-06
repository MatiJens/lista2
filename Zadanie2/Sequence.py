from abc import ABC


class Sequence(ABC):


    def __init__(self, identifier : str, data : list, VALID_CHARS : set):
        self.identifier = identifier
        self.data = data
        self.length = len(data)
        self.VALID_CHARS = VALID_CHARS

    def __str__(self):
        return (f"> {self.identifier}\n{self.data}")

    def mutate(self, position, value):
        if isinstance(position, int) and isinstance(value, str):
            if value in self.VALID_CHARS:
                self.data[position] = value

    def findMotif(self, motif):
        motifPositions = []
        for i in range(self.length):

            if self.data[(i - 1):(len(motif) + i - 1)] == motif:
                motifPositions.append(i - 1)
        return motifPositions