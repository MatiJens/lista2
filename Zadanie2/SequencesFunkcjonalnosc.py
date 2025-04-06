from Zadanie2.DNASequence import DNASequence

DNA1 = DNASequence("DNA", ['A', 'T', 'G', 'A', 'T', 'C', 'T', 'A', 'A'])
print(DNA1)
DNA1.mutate(2, "C")
print(DNA1)
DNA1.mutate(2, "G")
print(DNA1.findMotif(["T", "C", "T"]))
print(DNA1.complement())
RNA1 = DNA1.transcribe("RNA")
bialko1 = RNA1.translate("bialko")
print(bialko1)