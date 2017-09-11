# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 10:26:10 2017

@author: ASUS
This code snippet finds the open reading frames and prints possible amino acid sequences
"""


#Below function is inspired from the REVC-Complementing-a-Strand-of-DNA.py
def take_reverse_complement(string):
    #Take the reverse
    reversed_string = string[::-1]
    
    #Create a dictionary
    complement_dict = {'A':'T','T':'A','G':'C','C':'G'}
    
    #Take the compelement of the reverse
    complement_reversed_string = ""
    for base in reversed_string:
        complement_reversed_string += complement_dict[base]
    return complement_reversed_string

stop_codons = ['UAG','UGA','UAA']

rna_to_aminoacid_dictionary =  {'UUU' : 'F', "UUC": 'F', 'UUA' : 'L', 'UUG' : 'L', 'UCU' : 'S' , 'UCA' :'S', 'UCC' : 'S', 'UCG' : 'S', 'UAU' : 'Y', 'UAC': 'Y', 'UAA': 'STOP' , 'UAG': 'STOP', 'UGU' : 'C', 'UGC': 'C', 'UGA' : 'STOP', 'UGG': 'W', 'CUU' : 'L', 'CUC' : 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'CAU' : 'H', 'CAC':'H', 'CAA':'Q','CAG':'Q','CGU': 'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}

fasta_formated_input = ">Rosalind_8160\nTGTTGATCTCACCCGCTAGGCACGCTAGGTATATAACCCGCAATATGCCGCGCCGAACTCCTTTTGTGGATTCTAAGGAAGAGTGCACGCACCGACTCCCAATCGGGTGCGGGATTCGTGTCGTCCTTGCGTAAGCCTGGGGTTAGTTATCATGACGGATCCCGGGTCTAATCTCCCTTGCTACATGAAGCTCCCCTACCTCAGGGTCCAGCCATAACGGCAAGACGCGTGCTAAGCGTACAGAAGATCTATGTCCATAGTAGACACTCGCACCATAGCCTGGATGACCGCTCTTGGAACCGGTCCGTGCCCCTATGCGCATGATGTCCCGAGCGGGTGATTTGCGTAACCCACTTACGTGGATGAGACAAATTGTAAATGCCTGTGATCGGCCACAAAAGAGTTTCGGAATGAATGAATTCGTCAACGGTGCGAGTGCGGCGTAGCTACGCCGCACTCGCACCGTTGACGAATTCATTCATAAGAGTACATAACCTACTGTATACAAACGCCGCATGAACGTAGGCTTTATGACAAAGTGTCTTTGGCGTGTAACGTTAACTGTAAACTGATTATCCTGCGAGGTTCATTTCTTCTTAGGGCAAGGGGATTACCCTCTCCCGAACCGCATGATAGTCAATGCATGGTTATTGTGTATGAGTGTTCCTTGCGATGCTGTCCACGTTCCAACCTCAAATGTATTAGGTTCATAAAGTTGTTTTGGCCTTTGCGTCGGGAACACAAAGGCGTCGTGGACGCATTGAAGTTTAAGCCTTTGGAGACGAAGATACTTGCGGCCGGCATAGACGGCATGTACGGGTCGCGAGAATGGGATTAGCCAGTGGTTAGACCTCCAGAGTTAAGAAGGGCTTTTACTCCAAGGTTTTTTGTG"

#Coding DNA Sequence is provided
dna_sequence = fasta_formated_input.split("\n")[1]

open_frame_array = []

#Two loops: one for direct one for inverse direction
for reverse_or_direct_index in range(2):
    
    #Second loop will be dedicated for reverse direction
    if(reverse_or_direct_index == 1):
        dna_sequence = take_reverse_complement(dna_sequence)
    
    #Coding DNA is turned into mRNA
    mrna_sequence = dna_sequence.replace("T","U")
    length = len(mrna_sequence)
    #Three possible reading frame will be checked
    for j in range(3):
        
        
        last_codon_end = length
        #Very first loop is the standart one
        #In second and third loops, end of the last codon will differ
        #Refer this http://www.cs.wustl.edu/~cytron/101Pages/f13/Modules/3/Extensions/frame.jpg
        if(j != 0):
            last_codon_end -= (3 - j)
        result = ""
        start_reached = False
        #Reading frames start with 'j' end with last_codon_end
        for i in range(j, last_codon_end, 3):
            #Codon is extracted
            codon = mrna_sequence[i: i + 3]
            #If we already encountered with a start codon
            if start_reached:
                #If we see a stop codon than we created a open reading frame
                if codon in stop_codons:
                    #Stop reached
                    start_reached = False
                    open_frame_array.append(result)
                    result = ""
                #Otherwise keep on creating a sequence
                else:
                    result += codon
            #If start codon not yet seen, look for it
            else:
                if codon == "AUG":
                    start_reached = True
                    result += codon
#Get rid of duplicates
open_frame_array = list(set(open_frame_array))

#Amino acid sequences will be hold in this list
open_frame_protein_array = []

#mRNA sequence is translated into aminoacid sequence
for seq in open_frame_array:
    result = ""
    for i in range(0, len(seq), 3):
        result += rna_to_aminoacid_dictionary[seq[i: i + 3]]
    open_frame_protein_array.append(result)
#Multiple start codon situation is handled
for seq in open_frame_protein_array:
    for i in range(1, len(seq)):    
        if seq[i] == "M":
            result = seq[i:]
            open_frame_protein_array.append(result)
#Get rid of duplicates
open_frame_protein_array = list(set(open_frame_protein_array))

#Let's print those out
for protein in open_frame_protein_array:
    print(protein)
