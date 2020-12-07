#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

import colored
from time import sleep

# decoration
print(colored.stylize("\n---- | Transcribe DNA strand into mRNA | ----\n", colored.fg("red")))

# user interaction
dna_strand = input("Please enter DNA strand: ").upper()

# transcription standard
standard = {
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G"
}

def transcribe(strand):
    new_strand = ""
    for i in strand:
        new_strand += standard[i]
    return new_strand

mRNA_strand = colored.stylize(transcribe(dna_strand), colored.fg("red"))
print("\nTranscribing DNA ...")
sleep(2)
print("Transcription done.")
sleep(2)
print(f"\nDNA strand: {dna_strand}\nmRNA strand: {mRNA_strand}\n")
