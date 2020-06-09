# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:43:24 2020

@author: Austin
"""

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
         count = float(count + 1)
print(count)