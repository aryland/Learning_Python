# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:08:36 2020

@author: Austin
"""

import urllib,json

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print( 'Retrieving ',url)
    url_handle = urllib.urlopen(url)
    data = url_handle.read()

    print ('Retrieved',len(data),'characters')
    json_data = json.loads(data)
    #print json.dumps(json_data['comments'], indent=3)

    comment_count = len(json_data['comments'])
    print ('Count:',comment_count)
    
    comment_sum = 0
    for comment in json_data['comments']:
        comment_sum = comment_sum + int(comment['count'])
    print ('Sum:',comment_sum)
