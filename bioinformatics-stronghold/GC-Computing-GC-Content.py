# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:33:21 2017

@author: ASUS
This code snippet finds the maximum GC Content of the array of the DNA sequences in FASTA format
"""

string = '>Rosalind_1701AATCCAGGTCCTAAAGAAGCCTAAATATGGGCGTTCGCAAACGCTCTCGGACAATGAGTAGACGTCAAACCTCGAAACCCAAGTAACAAGTTGGTTCCTACCATTGTTGCTAAGGCTGAGAGGGGGCGCTAAGACTCCGGGCCCTCCTCATTTAAAGATAATATTAGGACTTGGGGTTGAGTTCGTCTCGCCGTCCGCAGCTTTCAGTGAACGATAGATCAGTTTAAATTCGTGCCTGCTCCATTGTAAGCAATTGCGCGAGTAACGTAAATGCGTTGGAGAACGGGGCGATGAATCGAGTACTTTCAAGAAAAACTCGAAAGTTCGCTTATGGAAAGTGCTGAGCTTGCGCCAGACTGGCGATCTGGCAAAGCAGACTTAGACGATCCTTCGAAGGGAATTACGGTACCAAGCTAGGAAAGTGCAAACATTTGAAGTGACAAAAGGGCGTGGATCTACACGCAATTCTGGCTGAATTAGATTAGATGAACGCAGCTGGCGAGGTTCTTAGGCCTCAAGCACGTCGCCAGAACCTACGCAAAACCTGTAGACTTAAAAAGCGTGGTAAACACTTCCGGGTCAGATTCGCCTGACTCTATGCAAAAGAAGAATCACATCGCAGAAAGAAACACCCATCAACCCACTTTGTTCAGTGAGGCTCAGTGCCTGGAACCGTTCGTCCTTGAATTACCGCCATCATTGTTGGATGGTTCGGCTTAGCCCGACCAGTTGCGGCGTTGTCGTCAGATCAAGAGACCATGCGTTGGGGGCAACGTTAATTGATCAATTTTTTTCAAGCCGAAACGGCACTACAGCTCTCTCAAAGATTAAACCGCTTTGGCTTTAAGACCTCATTATTTGTGCTAAGGCCGTGCTTT>Rosalind_5772CCGGCGTTGTATATCTTATCGCCGCCCTACGCCCTTGTAACTGTGATTGCAAGTTATCATTCACCGTCTCGCGGGCGGCTGTGGGGTTATCTTCAGAAGAAGTAGAACGATATTGTAGGCTCGGCCCCTAGGCTGGGTTAACCACGTAAGGAGGGTCTAATTACAAAATCTGTATGCCAGTTGGTTAACCCTGCGCCGTGGGTTAAACTTATTCGCTCTAGCCTTGAGTCAGCCAGGTATGACCAGATAATTCTTGGTAGGAGCCTTCTGGGAGGTTCAGATGGATCCGTGCCCCAAAGATTCACGCACTTTTCCGTCTAACGGTTAGCTCCAGCTCTAGTGGCACCGGTGAGGGCTCGTAAGGACAAAATTTTACGTCCCTGACTATCGCCAGATACAGTTGTTAGCGCCTGACCTCCTTACGTGATTAATGCCGTTACCGACATGCACAGTAGGGAGAACAAGCCGTTGTCGTTGTCCATGGAATTTACGCTCGTTCGAGCATCATTGCTAAGGGAAAAAAACGGCTGAGCTCCGCAACATACATGATGTATTGCAGAAAATACCTTTGTGTAGATGCTATCGAGGTCGTTGGCAAGCTCACAATTGCATAAGACTGGGAGTCCGTTAAGCTACACCGGGGATTAAAGTGCACGACGATCCAGATCTGTATAAGTGCGAGTGCAGAAAAGGCAAGACAGCCGAACTGGGGGACACTGTGGGGTATTTGCATTGCTTATCATTTCTTATTCCCCCAGGAAGCCCGGTAATATTCTTGTCCTATCCGCGGATGCCCATATCCACTGCCCAAGCTACGCGCTTAAGACCCATGTCGGCTCTGCGCAGGGTGATTCGCGGTGAAATCCGCTGCCGTT>Rosalind_6253GGTGGCTTCACATATGCCCGACGATCTGACGGCCCGGAAGTTAAACAGCCGTAGAATCCGTTCTTGTTGGACGGAATTGCGAGCAAGTCCCAGCTGCTAGGCGGTAGCGGAGTGCACGTGACAACCTTGACCGGAGCGCCATCCCCCCAGTGAAGGTCACGTGACATTGAAAAAGAGTGAATCACATAGGGATTTCCCATCTAGATTTTGTTATGTTCAACGCTGCCGCCGCACCCTACATATATCGCGGTTAGCGGTGAACGAGTACCATGGTCTGCGACTGAAAGAGGCGGGCTTTGGGCCTTATTCTGCAGGTCATTGTTTGACCGAATAATTCGCATGGATAGCACGGGCGGAAGACGATAATGCCGGACACGCCGTATATGTCCCATCGCTAGTTGTCTTTAGGCCGTAGATAATAAGATTGAGCGTGTTGCTGCCAGTGTGCGGGCTGGAAGCCCATTCTAAGTTAAGCAACTTTGCCGTCTGCGGATTACCTACCCAACTTCAAGACCTTGGTTTCAGTCGTCTAGTCTAATCGATTTAGCTACGCCGTCTGCCTAGCGTTATTAGATTGCTGCCAAGAGTACACGGAACTCTTACACAGCGAAGACCATAAGTAAGAGAAACGCTCTCAAATGAGCATACTGATGCGCGCGCACGGCATTTTTGGAGAACAACGGCCTCTCGTCAAAGTACATTGTCCTGGTTCCTGCAAGTCAGAAGTGGTGGTCCGAACAGTCAACTATCGGATAGAATATGCAATATTATGCTGATCCCACTCATCCTAGGGCGCCTCTAAAAAACGTGCATATATAGCTAGACTCGCCGAACGGAACTGTTCGGCATTCCAAGCCGGCC>Rosalind_1159TTTTTTCGCGATTATGCGTGATTTAGCAACCTGTACTTGATGGCTAAATTATGATGACGCCAATTATCCGTCCCACCCAACAAGTTGCAACTTTCCAGTCTGCCCAATACGATCGATCGTTACTTGTTAGAGTACGCCACAACCTCTTAAGGGATGTCTTGTACGTCAAGCTGGCTGTTTGTCAGATGCAAAATTCGGGACATTTAAGCTGAGAGAAGACAATCCCCAAGCCCCTTAATACAATACCAAGTCACACAACTATCATGGATTTATTAATTCGGCGTGGCATGACTATGTGGGAAGTGCATAATCGGAGCGGGCTCCTTCGGCTTGGACTCAAAAAAAGGAGCAAAGCTCACAGATATCTATAAGACATTGCCGAGCGACGGCTTCACTCGTACTTCCCCCAGCTCAAGGCACCTTCCCCTACCGGTATATAGGCTCTCCCTTCATACTGCAAGGCTGGGGTTCAGCCAGTCTTCGAGACGGTGTGACGGTGCTCTTTAGGTAGCTTGGAGGTCAAAAGGTAAGCGTTAACCCAGTCCCCTGGCACCGCTCTCAGTGCCAATAAACGGAAATGGGATTAATGTGCCTAGTGTAAGTCTCGGGTCCTATACTTTCAGCTTCCCGCAACACGACCATGGCAGTGGTTGCATAGTATGCACGCGAATCACACAAGAACGTTTCTACATAGTGTGATGTAATTACGATTGCTGTCCAGACGTTGTGGTCACCAACGTACCCCAAACAGCCGCCGTGCCTCAGAGGGATGCGTAACGGCGAAACGACGAAGCGCGCGGGAACTGTTCAATTGTTGACGTTGTGCCCAATCAATATGCAAGCGTCGCAACAATCGCCTTCCATCAGCCCAATAGCTCTTCGCACTCGCGTTGTTGAATAAGGGCAGCACAATTATGTGCTGTCACACAGCCGATACGTCCAACCTATTGGTTCGTTCGAGCTCGTGTGTTGGCTTCCAGCAACTCGTCACGTCAA>Rosalind_3369CGGGGCATGCACGCCTTAGCATATACATATTTTAACTTAGACATACACACTTACCCTGACCTCCGGTGACCTGCAGGGCGGTACATGCCTACATAGCGATGAAACTTGCGCATAAACAGAGTAGTGAAGCGGTAATGCGCAGGACAAATGGCTAAAAATGATAGATTATTTTGTGGGGTAGGTGTCGCTGGCAGGAACACTTAAAAGCAGTCGGTGTCACGAGATTAGGGTCTACGACGAGGAGCCGGAACGTTAATAGAGTATCCGCACGGCATGTTCGTAGCGTGACGAAGTCTCATGCTCTAGGAGAAATACAAAGAGTATTACAACTAGGGCTTCGCAGCAGCGAACCTTGTGCTGACATGCGCTTAACCCGAAACAATATGAGCGGGTTCAACTTGCCAGATTGCCCCCTCTATCGCCAACCCGGTCCAGGATCTTTCCGTCTCCCATCCTGACGTCAGTCTCGCGCCAAGCGTATCGACTAAAGCACCAGCCAATCCGAGTGACCGAGCAATAAATCGTTGGGATCCGTCCGTGTGAGAGAAGTTTCACGTAGTAAAGTAAGGTCCTTGTACGATTTGATGCGTTGGTCTCTAGCTTCCCGCCAAGAAATCAATTGAGTTCGCAGAGTCTTGATTGGCAGATGTGGACCGCATTAACTGGGAGTGCGGTATATAATATGTAGGGCCTGGGAACCGTGAACTCTCCCCTGGTCGGCACACCGAGACCTTCCGAGGGGAGGAGGCGATTCAACTCGCATACCCTCTGATATATTACAATTCCACCGGAGCAGCATAGGAGTGGATTGCGGGCCGTTGGCACAGGTGACATGGCCTACGTATCCGTGTAATTTCAATTCGG'
start = 0
#As long as there exist a '>' symbol after the start index
array_of_pos = []
while( string.find('>', start) != -1):
    
    pos = string.find('>', start)
    #print(pos)
    
    array_of_pos.append(pos)
    
    #Start index is assigned as the pos + 1 to search for next '>' symbol    
    start = pos + 1

def calculate_gc(string):
    gc_amount = 0
    for base in string:
        if base == 'G' or base == 'C':
            gc_amount += 1
    return gc_amount / len(string)

maximum_gc = 0
maximum_gc_id = ""

for i in range(len(array_of_pos)):
    pos = array_of_pos[i]
    ID = string[pos + 1 : pos + 14]
    #print(ID)
    substring = ""
    #Substring is obtained
    if( i != len(array_of_pos) - 1):
        substring = string[pos + 14 : array_of_pos[i + 1]]
    else:
        substring = string[pos + 14 :]
    #Gc is calculated
    gc_content = calculate_gc(substring)
    #Gc is checked to know whether it is the highest
    if(maximum_gc < gc_content):
        maximum_gc = gc_content
        maximum_gc_id = ID
    #print(gc_content)
print(maximum_gc_id)
print(maximum_gc * 100)
