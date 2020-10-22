# DNA Toolkit file
import random
import collections

# Adenine, Cytosine, Guanine, Thymine
nucleotides = ["A", "C", "G", "T"]
reverse_complement = {"A":"T", "T":"A", "G":"C", "C":"G"}

# Create a random DNA string
def createRandDNA(num):
    return ''.join([random.choice(nucleotides) for nuc in range(num)])

# Validate the sequence
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq

# Count the nucleotides' frequency
def countNucFrequency(seq):
    countFreq = {'A':0, 'C':0, 'G':0, 'T':0}
    for nuc in seq:
        if nuc in nucleotides:
            countFreq[nuc] += 1
    return countFreq

# DNA -> RNA Transcription
def transcription(seq):
    # U = Uracile
    return seq.replace("T","U")

def reverseComplement(seq):
    return ''.join([reverse_complement[nuc] for nuc in seq])[::-1]