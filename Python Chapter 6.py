# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:14:46 2020

@author: Austin
"""

text = "X-DSPAM-Confidence:    0.8475";
pos = (text.find("0.8475"))
#print(pos)
piece = text[pos: ]
value = float(piece)
print(value)