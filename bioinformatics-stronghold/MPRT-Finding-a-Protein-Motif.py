# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:17:05 2017

@author: ASUS
This code snippet finds the positions of occurences of N-glycosylation motif
"""

import urllib.request as url
import re

#Proteins are imported manually
proteins = 'P00740_FA9_HUMAN\nP07987_GUX2_TRIRE\nP01042_KNH_HUMAN\nP39873_RNBR_BOVIN\nP11171_41_HUMAN\nQ3BN23\nA6UUD2\nP20840_SAG1_YEAST\nQ3ATP6\nB5FPF2\nP01047_KNL2_BOVIN\nA6LJ74\nB5FNU0'
#They are splitted into a single protein
protein_list = proteins.split('\n')

for protein in protein_list:
    
    #Page is fetched from the url
    link = "http://www.uniprot.org/uniprot/"+ protein +".FASTA"
    fasta_format = url.urlopen(link).read().decode('utf-8')
    
    #First line of the page has nothing to do with the sequence it is just a header
    sequence_less_part = fasta_format.split('\n')[0]
    
    #Sequence is parsed
    #.replace("\n","") part is added because sequence is interrupted by them
    #and they need to be dropped
    sequence = fasta_format[len(sequence_less_part):].replace("\n","")
    
    #With a regex pattern iterator object is created
    #'?=' in regex added later having been realized( thanks to http://rosalind.info/problems/mprt/questions/) that without it regex does not look for overlapping occurence
    #'?=' idea is gotten from https://stackoverflow.com/questions/5616822/python-regex-find-all-overlapping-matches
    iteration = re.finditer("(?=(N[^P][ST][^P]))",sequence);
    
    result = ""
    #Every position of the occurence of the motif will be added to the result
    for a in iteration:
        result += str(a.start() + 1) + " "
    if result != "":
        print(protein)
        print(result.strip())
