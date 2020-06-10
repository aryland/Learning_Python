# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:37:45 2020

@author: Austin
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


#import urllib.request, urllib.parse, urllib.error

#fhand = urllib.request.urlopen('')
