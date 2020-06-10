# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:54:49 2020

@author: Austin
"""

largest = None
smallest = None
while True:
         try:
             num = input('Enter the number: ')
             if num == 'done':
                  break
             n = int(num)
             if smallest is None:
                  smallest = n
             elif num < smallest:
                  smallest = n
             if largest is None:
                  largest = n
             elif num > largest:
                  largest = n
         except:
             print('Invalid input')
print("Maximum is", largest)
print("Minimum is", smallest)
