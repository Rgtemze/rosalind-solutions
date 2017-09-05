# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:50:59 2017

@author: ASUS
This code snippet applies the Mendel's First Law
"""
#We will find the posibility of aa and subtract it from 1 to find the possibilites of AA and Aa
#A -> dominant, a -> recessive

#Below indicates # of AA
Homo_org = 27
#Below indicates # of Aa
hetero_org = 24
#Below indicates # of aa
homo_org = 23

number_of_org = Homo_org + hetero_org + homo_org

def combination_2(number):#Equivalent -> C(number,2)
    return (number * (number - 1)) / 2 

#Two individuals are selected
all_posibilities = combination_2(number_of_org) # C(number_of_org, 2)

#First possibility is that if two aa mates, it is 100% we will have aa
possibility_one =( combination_2(homo_org) * (1.0)) / all_posibilities

#Second possibility is that if Aa and aa mates, with %50 of possibility we will have aa
possibility_two = (hetero_org * homo_org * (0.5)) / all_posibilities

#Third possibility is that if both are Aa, with %25 of possibility we will end up with aa
possibility_three = (combination_2(hetero_org) * (0.25)) / all_posibilities

#1 - possibilityof(aa) = possibilityof(AA) + possibilityof(Aa)
#implied from possibilityof(AA) + possibilityof(Aa) + possibilityof(aa) = 1
possibility_of_dominance = 1 - (possibility_one + possibility_two + possibility_three)

print(possibility_of_dominance)
