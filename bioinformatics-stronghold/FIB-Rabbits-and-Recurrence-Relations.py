# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:58:50 2017

@author: ASUS
"""

n = 36
k = 5

#On the very first month all we have is one unmature pair
prior_pair_reproductive = 0
prior_pair_child = 1
#From 2nd day thorough nth day
for _ in range(2, n + 1):
    
    #Pairs that were child previous month will become reproductive
    #Also we should add previous reproductive pairs
    new_pair_reproductive = prior_pair_child + prior_pair_reproductive
    
    #Each pair will produce k amount of child
    new_pair_child = prior_pair_reproductive * k
    
    #Print them out
    print(new_pair_child + new_pair_reproductive)
    
    #Update the prior ones
    prior_pair_child = new_pair_child
    prior_pair_reproductive = new_pair_reproductive
