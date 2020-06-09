# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:48:35 2020

@author: Austin
"""

#9.4 Write a program to read through 
#the mbox-short.txt and figure out who has sent the greatest number 
#of mail messages. The program looks for 'From ' lines and takes the 
#second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail 
#address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary 
#using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

namedict = dict()
count = 0

for line in handle:
     if line.startswith("From:"):
       words = line.split()
       email = words[1]
       count = count + 1
       #print(email, count
            
            
print (email, count)

for key in emailcount:
     print(key, counts([key])
           
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lemon = dict()
for line in handle:
     if line.startswith("From:"):
         words = line.split()
         email = words[1]
         for emails in email:
            lemon[words] = lemon.get(words,0) + 1
                

bigcount = 0
bigword = 0
for email, count in lemon.items():
     if bigcount is None or count > bigcount:
          bigword = word
          bigcount = count

print(bigword, bigcount)


largest = -1
bigemail = None
for k,v in lemon.items() : 
    if v > largest :
        largest = v
        bigemail = k
print(k, v)


                        
print(email)

largest = -1
bigemail = None
for k,v in lemon.items() : 
    if v > largest :
        largest = v
        bigemail = k
print(k, v)




largest = 0
bigemail = None
for k,v in lemon.items(): 
    #print(k, v)
    if v > largest :
        largest = v
        bigemail = k
#print(k, v)



name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lemon = dict()
for line in handle:
     if line.startswith("From ") :
         words = line.split()
         words = words[1]
         #print(words)
         
         #email = words[1]
         #onlyemail = email.split()
         #print(onlyemail)
         #email = words.split(
         #print(email)
         #for onlyemail in words :
         lemon[words] = lemon.get(words, 0) + 1

#print(lemon)

#largest = 0
#words = None
#for words,lemon in lemon.items() : 
    #if v > largest :
        #largest = v
        #words = k
#print(k, v)





bigcount = None
bigword = None
for word,lemon in lemon.items():
    if bigcount == None or lemon > bigcount:
        bigword = word 
        bigcount = lemon 

print(bigword, bigcount)




