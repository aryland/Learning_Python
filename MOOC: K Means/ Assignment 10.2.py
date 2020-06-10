# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:19:07 2020

@author: Austin
"""

#10.2 Write a program to read through the mbox-short.txt and figure 
#out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time 
#and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, 
#sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lemon = dict()
for line in handle:
     if line.startswith("From ") :
         words = line.split()
         words = words[5]
         hours  = words.split(':')
         hour = hours[0]
         lemon[hour] = lemon.get(hour, 0) + 1

list = list()

for h, c in lemon.items() :
        list.append((h, c))
list.sort()

#print(list)
for h, c in list:
   print(h, c)
