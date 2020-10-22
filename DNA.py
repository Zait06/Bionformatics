# DNA Class
import random
import collections

class DNA:
    def __init__(self,dnausr='',numusr=50):
        # Adenine, Cytosine, Guanine, Thymine
        self.nucleotides = ["A", "C", "G", "T"]
        self.reverse_complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
        self.dnaStr = ''
        self.rnaStr = ''
        if len(dnausr) > 0:
            self.dnaStr = dnausr
        else:
            self.createRandDNA(numusr)
        self.toRNA()

    # Create a random DNA string
    def createRandDNA(self,num):
        self.dnaStr = ''.join([random.choice(self.nucleotides) 
            for nuc in range(num)])

    # Validate the sequence
    def validateSeq(self):
        tmpseq = self.dnaStr.upper()
        for nuc in tmpseq:
            if nuc not in self.nucleotides:
                return False
        return True

    # Count the nucleotides' frequency
    def countNucFrequency(self):
        countFreq = {'A':0, 'C':0, 'G':0, 'T':0}
        for nuc in self.dnaStr:
            if nuc in self.nucleotides:
                countFreq[nuc] += 1
        return countFreq

    # DNA -> RNA Transcription
    def toRNA(self):
        # U = Uracile
        self.rnaStr = self.dnaStr.replace("T","U")

    def reverseComplement(self):
        return ''.join([self.reverse_complement[nuc] 
            for nuc in self.dnaStr])[::-1]