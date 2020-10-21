from DNAToolkit import *
from utilities import colored

if __name__ == "__main__":

    dnatk = DNAToolkit()

    randStr = dnatk.createRandDNA(50)

    DNAStr = dnatk.validateSeq(randStr)

    print(f"\nSequence: {colored(DNAStr)}")
    print(f"[1] + Sequence length: {len(DNAStr)}")
    print(colored(f"[2] + Nucleotide Frequency {dnatk.countNucFrequency(DNAStr)}"))
    print(f"[3] + DNA/RNA Transcription: {colored(dnatk.transcription(DNAStr))}")
    print(f"[4] + DNA String + Reverese Complemet:\n")
    print(f"3\' {colored(DNAStr)} 5\'")
    print(f"   "+''.join(['|' for _ in range(len(DNAStr))]))
    print(f"3\' {colored(dnatk.reverseComplement(DNAStr))} 5\'\n")