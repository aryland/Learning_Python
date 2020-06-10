# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:33:58 2020

@author: Austin
"""
#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt
print(line.rstrip())


fname = input("Enter file name: ")
fh = open(fname)
est = list()
two = est.sort()
for line in fh:
    stuff = line.split()
    stuff.append
    stuff.sort()
print(stuff)


fname = input("Enter file name: ")
fh = open(fname)
one = list()
for line in fh:
     words = line.split(' ')
     words.sort()
     words.append()
print(words)



fname = input("Enter file name: ")
fh = open(fname)
zst = list()
for line in fh:
     line = line.rstrip()
     words = line.split() 
     #alpha = zst.sort()
     #each = zst.append(words) 
     #alpha = each.sort() 
print(words)


fname = input("Enter file name: ")
fh = open(fname)
zst = list()
for line in fh:
     #line = line.rstrip()
     words = line.split()
     #print(words) 
     #alpha = zst.sort()
     #each = zst.append(words) 
     #alpha = each.sort()
     for word in words:
        if word is not zst:
            zst.append(word)

print(sorted(zst))
