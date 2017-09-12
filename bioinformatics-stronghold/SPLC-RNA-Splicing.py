# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:42:58 2017

@author: ASUS
This code snippet does RNA Splicing
"""

rna_to_aminoacid_dictionary =  {'UUU' : 'F', "UUC": 'F', 'UUA' : 'L', 'UUG' : 'L', 'UCU' : 'S' , 'UCA' :'S', 'UCC' : 'S', 'UCG' : 'S', 'UAU' : 'Y', 'UAC': 'Y', 'UAA': 'STOP' , 'UAG': 'STOP', 'UGU' : 'C', 'UGC': 'C', 'UGA' : 'STOP', 'UGG': 'W', 'CUU' : 'L', 'CUC' : 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'CAU' : 'H', 'CAC':'H', 'CAA':'Q','CAG':'Q','CGU': 'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}

#Input file is imported
file = open("a.txt", "r")

def extract_sequence_from_input(file):
    sequences = []
    result = ""       
    
    #For each line
    for line in file:
        #When encountered with a '>' symbol
        #We will assume we are done with a sequence
        #and we will add it to our list
        if ">" in line:
            sequences.append(result)
            result = ""
        #If line does not include we will collect the line
        #in the string called result
        else:
            #We should also avoid '\n' escape character in our dna_string
            #so if the line includes it we will remove it
            #Note that last line will not include '\n'
            #So I added else part
            if "\n" in line:
                result += line[:len(line) - 1]
            else:
                result += line
    #Also after the last line there is no '>' sign
    #so loop could not catch it
    #Hence, we have appended what is inside the result variable
    sequences.append(result)
    #When we first encounter with a '>' we will not have collected any dna string
    #so we will end up with an empty string
    #This code fixes it
    sequences.remove('')
    return sequences

sequences = extract_sequence_from_input(file)

#First part is the dna itself
dna_string = sequences[0]
#Following parts are the introns
introns = sequences[1:]
#Introns are sorted in descending order to avoid overlapping
#E.g DNA = AGCT INT1 = AG INT2 = AGC
#If we sorted in ascending order 
#DNA - INT1 = CT
#Then we would end up with a wrond solution, actual solution was T
introns.sort(reverse = True)

#We will remove the each intron from the string
for intron in introns:
    dna_string = dna_string.replace(intron,"")
dna_string = dna_string.replace("T","U")
#print(len(dna_string))

#We will print out the aminioacid sequence
#Note tha stop codon is removed from the loop this is what '- 3' has to do with the loop
for i in range(0, len(dna_string) - 3, 3):
    print(rna_to_aminoacid_dictionary[dna_string[i: i +3]],end='')
