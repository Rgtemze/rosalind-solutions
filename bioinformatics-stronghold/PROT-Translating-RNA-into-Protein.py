# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 10:20:19 2017

@author: ASUS
This code simulates translation of RNA into Protein
"""

rna_to_aminoacid_dictionary =  {'UUU' : 'F', "UUC": 'F', 'UUA' : 'L', 'UUG' : 'L', 'UCU' : 'S' , 'UCA' :'S', 'UCC' : 'S', 'UCG' : 'S', 'UAU' : 'Y', 'UAC': 'Y', 'UAA': 'STOP' , 'UAG': 'STOP', 'UGU' : 'C', 'UGC': 'C', 'UGA' : 'STOP', 'UGG': 'W', 'CUU' : 'L', 'CUC' : 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'CAU' : 'H', 'CAC':'H', 'CAA':'Q','CAG':'Q','CGU': 'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}

string = 'AUGGUAAAUUCAACUCGCAGACCUAUGCGAAGAUCGAGGCCGUCACCACGAGUAUGUCGAGAAAACAGUGAAUCCUAUGUCUGGCACGCCAGCAAGACUAGGUCAAACCCAGCCCUCAAAUGUAAUCAGGCCGGUUCCUCCGAAGGUUGCUUUCCGUUUUUACCAUAUAUUAGAGCCCGGGAAGGUGCCAACGAUGUUCAUUAUACAGGGGCUGCCCGCAGGCGUUCGAUGUGCAUAGGGAAGAGUGCGAAAGCACGGGGAUUAAGCUCCGGAGACUCAGCCGGAACCCAAUUCAAAUGCCAUAAAACUUUUAAAAUAGGGGCACUUCCGGACAACUUCAACUACGUGGUACUCCCGCGCGGAGCGGCACUCGGGUCAGUCUCGAGCGUCGGACCUCUCAAUGCCGCGUUACCAUACUUUUACGUCGGCGGGGUUCCUAGGAUUAGCUGCGUUUUGUGUUUUGAUUACGACUUUACCUUUGCGCCAACGUGCAGAUAUGAUCCGGGCCCCAUUAGUGUCUUUUGCAGGUCGUCCUUAUACGUGGCACAGGUUUGUACUCAAAAGAUCAGGAGGGUCACAUUAUGGUUGGACGAAUGGUAUCUUACAGAUAAGCAUUUCAUAAUGAAUGGCGCAAGUUGCACCUUACUUCUGGUUUACAUACGAACAUUCGCUCCAGAACCAACGGAUCAACCAUCCCGAGCUGGCUCCACUUGUGUUGUGUCACCCCUUCGCUCAUUACCUGCCAGAGAUGAAUCUCUACAUGUGGUUUUACUUAUAGGCGCGAGCAGUCCGCUAUGCGAUAGGGCCACCACCCCUAGUAGCGAAAUUAAGACCUUACGUACCGGGACGUCAACGAUUUCUCCGACGGGGAGUCUCCAGGCGAAGUCCCGGGCAGGUGGAAAUUCCCGGCAUAUAUGGGGGAUUGCGCUAUACUAUAGGAAGUAUUUGUUCAUAGUUCCAUCACCACCUCCCGUGGGGAUGUACAAACCACGUUUAACGACGAUCACAGGAUACAUACGUGGCCUCAAGCCCCAGUGUUCAGAUGGUAUAGGAGGUCAUACUUUAGGUGUCCUAGUAAUCCGAUGGUCCGGUUACGACUUUGAUUUAAUUCCUGCUUUACUACCGACACGACCUCGUACAGAACUGCUUCCCUUUGUGCGUGGCGUGUCACGACGCGGGGAGCAAUGGGCUUCGAAUGAUAAACCUGGAUCGUCGUCAGCCGUUGGGGGUUCAGGGGCGCCUGCACCCUGGGGACGAAAAGGUAAAAAUGCAGGAUUUUAUCUACGUAAAGGCUCCCCAAUGGAGCAAAUGAGUCGCGGGCAAAAGGCCUCAGUUGCCACUUACUCUACAGUCUGCGCACCAUCAUUGAGGCCCAGGCCCGAAGAUAAGGUCCCAGACGUAGUUGAUUACGGGGUGAUGAGGUGUGUAUCUAGAGUGAUCAAGCUGGCGACGUCCCCCGCCGGGCCAAUGAAUUCACGAGCAAUACUAACUUCGGGAUUCCGGGGGGGCACUAUUCGUAAUCUUGACAUUUUACCAACCACAACCGCAGGCCCAAGUUUCGCAUUGCGAGGUCCAUUGGUACUCCCCGUCAGGGCCGUGACCUUGGGUCCACAUAAGAAUCUAGCAAGGCUCACGAAAGACGUUUCACAUCCUGGACAGCGGCCGCUUUGGUGUUCACCCUCAUGUCCAACCCUUUGUGAAUUUCUGUUUUAUUUAGCUUUCCGUGAUACCAGUGUUUACUUUGUGCUUUCUAGUGUGUGGUGCCUACGGGUUGAAUCUUUGGGAGGUCCACGACUGCAGGAAUCACAUAUGCCGCAAGCCCCGGGGCAGGAACUGAUUUGGAUUGCAUCUAGCCACCCAUUAAAAUUUAACGCUCGAGCCGGCUCUAAGCGUGCUUGUGGACGACAUCGGUGGACGUGGAGCGAGUACCGUGACGUUUGCUAUUGUUACCCUAGAGGGAAUAACGCCUUACUUCCCCACGGACGAACUAGGUCGAGGGUUUCACCGGGCACUGUUGCUCUAGGAAGACUACUUAACAAGAUCGACCAAGCUGCUCUCCUCCCUUUCCGGAAGCCGGCAUGUUGUGAAGACGCUAUAACGGCUUUAGCCCAGCAUAGCUACUCGUCUAUCGAUAAUCCCCCGCGCCUUUUACACACUAGAACCCACCAUAACCCAAGCCUGAAUAGAGAUAACUUCUAUAUUGGGCAAUCGUAUUCUCGUUGUGAACAGGUCCGGUUCGGACGUUCCAGCACAUCUGGCUGCGAGAAUCGCACAGUAAAUUUCGAUAUGGGGCCACCAUCGGCGGCUCGAACAGUGGCAUGCGAAGUUUUGUGGAGCAAUCUUUGUCGAAGUGAUCAAUCUUCGCGGGCAUACCAACACGGUCGGCCCCUGCGCAGUUCGCUCGUCCGACGCAGCUGCUCAACGAUUACCGAAUCGGAAGUCCCCCAUGGUAAUCACCUUCAUAGUACGCUACUGCAUAGAACGCAUUGUGUCAUCUGGCUGUCACGGAUUCGGUGGAUUCUAAACUGCGGUCGCCCGGAGGCUGGAAUCCAUGGGCCCGGUCAGAGCAUGUCGUUUCCACCCAGCGUCAGCCAGUAUACCCAUGCGUUCUACGACGUCUCCGUCGAGGCGUUUAGUCGCUCGGGCCACCUCCACGUCACUCUCGCGCGAAGGUGUGUCAGUAUCAGGUCUCACACUCUCGGGACUUUUCGAUCAUACUUACCUGACGUCGCUGCAAGUUCCGACCGUUACGGGUUUGAUUGUUCGCUCUUGCCCUCUUCCCUUUGCGUGUUGCUGAACUCUACACUUCUUUUGCUGCAUGCGAACGUCUUGAGUUGUCCCAUCUCCCCUCGGUCGGUCGAGGGCCAUGGGCGUCUUUUAUCUUCUCCUAAGCGAAACUACCACCCAAAUACCCGUGACUGCAAGUCUGGUCCUAACGUAGGAAAACCUCUCAGGGAUCGACCGAUAUGCCGCGUCGGGCUACUUGCCACCGCUGAAUUCCUGCUAUGGGCGAUCGAUACUCGUCCAUCGUAUCAAGAGAUGGUGUGUGCUAGUGAUUACGUCACGAUCAAUCCCUUGACCACUCACAUCAUGCUUAACAUCCAUUAUUACUAUGUCUUGCUGUCCAAAGCCAUCAGGCUCCGGAGCCGCUGCACACAACGGUGCGAGGCACCGAUUAGCUGCCGAGGCUGGCCGGUUAAUCGCGGCCGAGAUCCCACUCACUGUAUUAGCAAGGGUGAGCUUAGCGCUUGUUGCUCAUACCGGUGCGAUGAAUCCACGAAACUGGCGCGUGAGAGACACAUGUUUUAUGCAAAGCACAUUCAGGUCAUAUGGAUAGUAUGGGAUCCUCUUCCAUAUAAGUACGCAUCUCGUACGUGGAGCGCUCCCUUUAGUCGACUGUUUUCUGGUGUAGAUCCGUAUUCUAGUGUGUCGACGAGGUCCACUAUUUCCGUCAGUGGAGCUUAUCCCAUCUUGACCUCACCCUCACUUGAUACGAGUGACUUAUACAUUAGGCAUGGCUUAGGACGGGCGCACCUGCCCGGCUGCAUAAGCUCGGGCACGAUGCUGGAUAGAGGAAAAGAAGAUCAGCGAUUAGAAGAUCCAUCUUCGACACAUCGGACAGGACCUAAACAAAUGUGGUUCUUUUUGCUCAGACAAGCCGGUCGUGGCGUAAAUCCUUGCAUAACUUUCAAAUCUCGACCGGAGGAUAACGGACAGUGCUGCUUUAGAGUUCGACGGUACGAGUGCUCUAUUAGAAAGGGGGUACCAUGUAUCCGUUUCUCGAUUCAAGAAGACUGUUGCCGGAUCAUACACACAGCCAUUCCAUCUAUAGAUUUACUCGUAGCACUGGCUUAUACGGACGUCCCCAUUUACGGAGUACGCCACGGCGAUGGAUGUAGUCAGGUUAUUAUCUCCCCAAAAGGUGACACGGGCCCUAUACGUGGCCCAAUUGUGCUCCGGGUACUGCGUCUCUCAGCUCGGGGAGUGAUAUGGCCGACACAACGACCCACAAAGGCUGCGUCCUAUCCUAGUGCUAGGUGCGCUCCCACUCUGUGUGCGCCCCCUGUUUUCGAUUCGUUGCAUCACCGAGUCCCCAAAUACUUAUUGGAGACGGGAGCAAAAAAACAAUUUAAAAGCGAGAAAUUGAUUUCCUUGAGCAGGUUACAAUUAGUCACUCUGGACAUCUAUACCGUGUCUAGCAGUCUAUUUGCACUGAGAUCGUUACUUUGUGGAAUUAAACGAAAUGAAAUCUACUUGCUGUGCAAACCGAGGGCAGCCAAGAGAGGAACGGAUGGCAUAGUGCCACUGGGGCAGUCCGCAGAGAUAAAGCAGCGUAUUCAUCACAAAUACUGUCUCCAUGAAGUAUUUGCAUAUAAUCACGUCGCUGACUGUCGAUUGAGGAUGAAUUUGGACGGCCAGUUACUCAUUACCAGGGGGCCAGUUUAUUUACGUUGCUACCAUACCCCUCAGACUCGUGCCCGCUCACAUGAAAAUCACCAGCAGAUCAGGUCACACGGUGCGAGCGUCAGCAUCGUUUCGGUGUGGCCCACUCUUCUGAUCGGGAAGGAGCUCCUCGCGGUAUGCUAUGUUACCACGCUGAGUCUUUCCAUCUAUUGGACGGAGAUCGGUCUUUCUACUCGUAUGCAUAUGACAACAAACCUACUGACCACUCACAUGUGCACGGAUUACGUGCAAGGCCAUGAACCUCGUCCACCUCUCGAAACAAUACAUAUUUCUCCGAUUAGCCGAAGGCCUAAUGAUGAUUCCUGUAGAUACGCAGGACCCUCGACACUACCACCACCCAUCGCUGCCCCUUCUGCCAGAGGUUCCAUUUGGCAGGUAGUACUAGAGGUACGAUGCCCUUUCCGGCUGCAAGAGAUACGCAUCUUGCAAGAUAUAGUGUCCACGGCCCGCACCUUCGCAAGACGGCGGACUAUCGGAUUUCUUGGGGGGAAUGAGAUCGGUCAUGUGCUUAGGACGGAGCGUGAAUCUAGUUUUGAACCUCCCCCCCGCCAACACCCAUACACUGUGAACGUUUUUGAUGGACGAGCCAUGAACCACCGCUGCGCGAGAGAGGUGGAGAAACGUGUAUCAAGGUACCAAGGCCCUGACACCGAUAUAAGAAAGCAUGAGCACUCUCAGUUACAACAACAAUCAAACCGUCAUUCAAUCAGUUGUUUGAGAGCUCCUGUCUAUCAUAGACGUAGAUCAAACGGGUAUGCAGCUCAGUUGUCUUUGUGCGCGACCUUCAUCCGGGUCCAUUGUAUCAAACAUAUUAUGCAUGAGAGGGCGUCACGAUCACCCUCCGAAGUUUCCUCAGAGUUACUUAAUUUCGCUGUAACAGGAAAGUUCCGACAGUCUCAAACCCGAACCAGACCUAUCCUGUCCAGCCGGGCAGGCACAUAUGGAUAUAGUCGCAUUUUCUGCAGUCCUGCUGAGGCGGCGGGUAUAGGAACACACCACAUAGCGUACUUCAAAGCCGAAGACAGCGACGACCCGGAGUGUGGCAAUCCGCUACACAGAAUCCUCGACGUCAAAAGGCUUUGCAUGAAAUCUCGGCGAAAAACCUUAGAGGGUUCCACGGUACCCCAAUUUCUACAAGCUGUUACCCGAGACAUGUCUCCAGGACUCAGUUGUGAAAGUACACGUCUAUUAUUAGAUGCGCGCUUCUGCCUCACCAGUCCUAAUGUACAACGGCUGGGUCUAUUAGGACUCAUUGUUUAUGGUAUUCUCGCGAUGGGCUGGUCUCCGCUUGAAAUGCACGCGACGGUUUCCUGUCAGUCGAACGGGACAGGGUCUCACGAACUAAGGAUCCUGUCUAGUAGUAUACGCAGUCAAACACAGCGAACACCGUCGCCAAUCGCCAUUUGCAACUGUCCUCACUGCCGCCUAGGCGAGUAUCCUAUGUCUUCGUGGUCCGACUACGGAGCUUCUAGCCCGUUAGAACGCCGUUUUAUAGCUACAGAUCGCGUUCAUGAAUAUGCAACUCGGGUCCUAUCUGCAGAAGUUCAGGCGCUUGCUGGAAAGUAUAUCCUUAGGAAGUUCGUUCCCGCUGCCGACCGUGACGUGGAAGUAACCGACACUGUGGUCGGUAUAAACGCCACCAGCAAGUGGAGUCACCAACGCGCUGGUUUAUGCGCCAUCCCCGCUUCCUGGGGAUUGCGGACAUACAUGGGAAAUCCAAUCGGUUGCAAAACGGAACACCGGCAGGCCGGCCAGUCCAAUUGUCGCGAGUGUUCGUUUACUAUGCCGCGUUACCAAGAGCAGGACGGUAGGAGCGGGCUAAGCGAUAAAGAGUCCGGAACAUUGUCACACCAGAAGUUCAGCCUGCAUAGACUCGUAAUUUGUACCUGGGGUAAGCUCACGGCUGGGCGCGCGAUCGUGGUACUCAGCCAAUUCGAGGGCGGCAGAAGACGGCUCUGGGCUUCAACCGGCACAAUGCUUAGCCGUACCCAGAGGUGCGCAACCACAAUAGACUUACGUAUAUUGUAUAAAUGUGAUUGCCGGUGCAGGAUGAGUGCAAAUGGCUCAACCGGCUGCUACGUCAUAAUCUGUAAUUUUGCGAACGGGACUAAUUUCGAUAGCUUGCAUGGUCUCGAACGUAACGCCCUACCCACACAGGCAGACUACUGCGAUCCUUAUCAGCACGCAAUUGACAGAGACGAUGUUACUUAUAGGAAACACAAAUCGGGGAUAGAUCGGUAUUUUGGAGUUUUCCUUAUGGAAAUCGCACGGGCGCCCCGUAUGCGUGUAGCCAACAUUGAGUCAGUUAUUUCGUCUGUAAACUAUGAAAUUUUACUGUUGAAUUUACUGAGUACCAGUAGCACGGUCGCCCAGUCCGCCUCAAGUGCUUCUUUAAUGAGGACUUUGCUACGGCUCGACGUAAUAAUCCUCCAGCUGGCAGUGGUCCAUAUACGCGUUACAAACCACGGAUUAUACCGCCAAUCUUCUACCCAGGUUUCUACUCACAGUAGCGUGUUGGGCAACCUUUCAUGCGUGCUGGGGAUGCUCCCCCAACAGCUCCGGCUUAGUUCGAGACCGUACAAUGGUGCCAACCGUGCAGAUAGCUCUCCGGAAUCUCAUCACAACUCGCGACAUAGCAUUCUGUUUGCGAGCAGAUUUCACAAAUCACGUCGUGACCAGGACUCCCUAUUCAGCCAGAACUUACCUUUUGCAAGUACAGAACGAUGCAUUCCGAUAUCUGGUUUGUUCUUCGGAGACCCCAGAUUCCCUCAUCAUGAUCGAGACCCAUGCACCUGCCAGCAUUUCUCUAUCUGGACGAGUCAGGCCCCCUCCCAGACUAAGAGCGGCACUGUUAGUUGCUUAAGCAUGGCAUAUUAUCUAUUCCCGCUCGUCACGCCCGUGUAUUGUGACCGCGUGCCGGGCUAUCUCUUCCCAAUUACACUUCGGGCCGCGUUCGAGGGGGGGGGGUUUCUUAGUAAAUAUAGCGACCAGCUCUCGGGCCUAUCACUCCCUAAAAACCCCUUAAAUAUAAUUAUCGAACGGUGGAAGGACUUGGGGACGGACUCCUCACAUUUCGCCAAGAUACAUGGCGCCGGAAACCAGAGGAUGGGACCUGACAUUGAAGACAAACAACAACCCACAUCGAUUUCGGUUUUCUACGCAGUUAUAGAGCGCCUUAGCGGUCUCAGUAACACGGUUAGAGCCACGCACCUAGACUACAGAGGCAUUGACAUAGACUGGCCAUGCUCCAUUUCCCACGCCUUGUCCCGUGCAGCCUUUUCGUCGGCGACUAGGCCGUGCACACGUGGGCAAGGAUCAAUCCACCAGGUACAUCGCCUUAUGGAUUAUGGAAACUGGCUGGUAAAAGGCGAUGCCCACAAAACCUACGGAUUAAUACCGUUACGUUGUGAAGGCAGGCUUAUCAUGCGCGCUGCUAUUUCAAUAGAUUCAUUAUAUCCGGGGAAGGCGUGGUCCAGGCAGAGCAAUCGGAGUUUGAUCUACGUGAUCCCCCCAUUCAACGCUGGCACGUUGCGCUAUCCACGCAAGCCUCGCGUGUUGACCAUCGCCGCCUUUAAGAAUCAUUGGCUGGGACAGUCCCAUUCGAUAUCCCGGAGUGCCGUUUACAAGCCGGAUGUCUUCUCGAACAUGAGGGCGUCCGCGCGCCUUGAAAGGUGUUGGUUAGAAACCUCAUACAAGUUCGUAUCGUGGAGAUCGUUACAUAUACAGGAUAAAACUAUUGGUGUUGGACGUGUAGAAACCGGACGUAAGGUUAUGCUGGACGCUCGUUUAGGGGGGGCUCGGCGAGCGUCAUUGACCCAACCACAGUAUUGUUCUGGGCGGCAUCUGAAACGCUCCUGCGCAGCACACGCCCAGCCUACGAACAGUCAAUUGUCCUCUCAAUGGGACUAUUGUCAUAGUGUACUCUGGGGUCAUGAGGCGCCCGAAGGACCUAAAAAAGCGCCUCUAACUGAUGUCACAGUCAGUUUUAGUACCGUGGAUCGGGUCACCUCGUUCCGGUUAUGGAACUUAGCGGUUAGGCGAGCGGCGUUCAUACGAAAUCAGAGGGGUAAGAAACGGAUCGCGUCCCUCACCCUUUGGGCCGCACAUAUUGAUUGGGCGAUUAUAACUAGCCUGGCAAUGGUUUGUGCCCUCUACCGUGGUAGAAGCGGAUUGGUCUCUCGCUCGGGCACAAUUCUUCCAGACGCAAUUAGAAUUCGUCCACCCUACUGGCUCCGAGCCCCGGCAUGCUCAAACUUAUCGCAGAAGAUAUCCCACGAAGUCAGGUUUCCAACAAUGGGUUAUCAACGACCGCAUGUCAUUCGCUGCCUGUUAGGCGCACUCAUCGGGAGAUGGGUGAUAUUCCCUAAGAAAUUCAGCCGUAGGAUGCAGUAUGGCAUUGAAACGUGCCGCGCUAUCCCCCCCGCUUAUAAGUUCGUAUGCCGCUUCAGUAAGAUUCCGUGGGUCCUGACGAGAGGGAGUUCAUCUCGUUCUUGCUACUCAAUAAUGACGGCCCAGUUUGUGCUGCACGGCAGUCCCGCGAGGGGCACUGGUAUAAGUGGAAUCAAUCAAUGGCAAACUAUACAGAAGGUAGGUCGGUGCACGCCUGCCAAUCAGGGCGCAGAAGACUGUUUGGCAUUUAGGACUCGGAGCAAGGGUCGUCGACUACUAAUACGUCUUAGUUUCGGAAGCUCUCCAGAGAGGGUUACCGCUGUGACGGUAAUGAUGAUUAAUCACCUAAGGGUAAUUAGUUAUACCCAAAGUAUUAGCAGGGUCCCGAUAGCACAGCGACCUCUUCAGCAAUGUCUCGAAGUGCACAAUCGAAGAAUACGAGUGGAGGGACUAGGUAUUAUUCACCUUCGAUACCAUGUUUUUUCACCCUACAAUCUAACGAGUAGUGUGUCGAAGAAGUUGACUAGAGGUUUCCAGACACUUAAGCUGUAUGAGCAGAAGCUAAGCCCUACGAAACGAUCAGCUGUACUGCGUGCAUAUCCUAUAGAGUUAAACCGGACUCUGGUACGAUUUUGCUCCGAUGGGCGACUCACCUGUGUCACCAGAGAGGGGGGCAUCGACUCUGCCAGGGUCCGGUCGGGACGUAAGGAUGGAUUCUAA'
aminoacid_sequence = ""
for pos_of_codon in range(0, len(string), 3):
    codon = string[pos_of_codon: pos_of_codon + 3]
    if rna_to_aminoacid_dictionary[codon] == 'STOP':
        break
    aminoacid_sequence += rna_to_aminoacid_dictionary[codon]
print(aminoacid_sequence)
