import pytest
from Zadanie2.DNASequence import DNASequence
from Zadanie2.RNASequence import RNASequence
from Zadanie2.ProteinSequence import ProteinSequence

# DNA

def test_dna_init_valid():
    dna = DNASequence("seq1", ["A", "T", "C", "G"])
    assert dna.identifier == "seq1"
    assert dna.data == ["A", "T", "C", "G"]
    assert dna.length == 4

def test_dna_init_invalid():
    with pytest.raises(ValueError):
        DNASequence("seq2", ["A", "T", "B", "G"])

def test_dna_complement():
    dna = DNASequence("seq3", ["A", "T", "C", "G"])
    assert dna.complement() == ["C", "G", "A", "T"]

def test_dna_transcribe():
    dna = DNASequence("seq4", ["A", "T", "C", "G", "T"])
    rna = dna.transcribe("rna_seq")
    assert isinstance(rna, RNASequence)
    assert rna.identifier == "rna_seq"
    assert rna.data == ["A", "U", "C", "G", "U"]

# RNA

def test_rna_init_valid():
    rna = RNASequence("rna1", ["A", "U", "C", "G"])
    assert rna.data == ["A", "U", "C", "G"]

def test_rna_init_invalid():
    with pytest.raises(ValueError):
        RNASequence("rna2", ["A", "X", "G"])

def test_rna_translate():
    rna = RNASequence("rna3", ["G", "C", "A", "A", "U", "G", "G", "C", "U", "U", "A", "A"])
    result = rna.translate("prot1")
    assert isinstance(result, ProteinSequence)
    assert result.data == ["Ala"]

def test_rna_translate_no_start():
    rna = RNASequence("rna4", ["G", "C", "A", "A", "U", "C", "G", "C", "U", "U", "A", "A"])
    result = rna.translate("prot2")
    assert result == "brak kodonu startu"

def test_rna_translate_no_stop():
    rna = RNASequence("rna5", ["A", "U", "G", "G", "C", "U", "G", "C", "A", "A", "G", "C"])
    result = rna.translate("prot3")
    assert result == "brak kodonu stopu"

# Protein

def test_protein_init_valid():
    protein = ProteinSequence("prot1", ["Met", "Val", "Gly"])
    assert protein.data == ["Met", "Val", "Gly"]

def test_protein_init_invalid():
    with pytest.raises(ValueError):
        ProteinSequence("prot2", ["Met", "ABC", "Gly"])