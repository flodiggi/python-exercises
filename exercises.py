#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:35:25 2018

@author: flo
"""

#%%

def linear(lst, elem):
    for i in range(len(lst)):
        if elem == lst[i]:
            return i
    
    return None
#%%

def hello():
    name = input("What's your name?")
    print("hello" + name)

#%%