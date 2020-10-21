# DNA Toolkit file
import random
import collections

class DNAToolkit:
    def __init__(self):
        # Adenine, Cytosine, Guanine, Thymine
        self.nucleotides = ["A", "C", "G", "T"]
        self.reverse_complement = {"A":"T", "T":"A", "G":"C", "C":"G"}

    # Create a random DNA string
    def createRandDNA(self,num):
        return ''.join([random.choice(self.nucleotides) 
            for nuc in range(num)])

    # Validate the sequence
    def validateSeq(self,dna_seq):
        tmpseq = dna_seq.upper()
        for nuc in tmpseq:
            if nuc not in self.nucleotides:
                return False
        return tmpseq

    # Count the nucleotides' frequency
    def countNucFrequency(self,seq):
        countFreq = {'A':0, 'C':0, 'G':0, 'T':0}
        for nuc in seq:
            if nuc in self.nucleotides:
                countFreq[nuc] += 1
        return countFreq

    # DNA -> RNA Transcription
    def transcription(self,seq):
        # U = Uracile
        return seq.replace("T","U")

    def reverseComplement(self,seq):
        return ''.join([self.reverse_complement[nuc] for nuc in seq])[::-1]