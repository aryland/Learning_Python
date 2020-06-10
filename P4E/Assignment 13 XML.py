# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:04:27 2020

@author: Austin
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#sample data
#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

#actual data
url = 'http://py4e-data.dr-chuck.net/comments_363814.xml'

data = urllib.request.urlopen(url).read()

#data = urllib.request.urlopen(url, context=ctx)

tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0
for count in counts:
    total += int(count.text)
    
print(counts)
print(total)
