# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:14:16 2020

@author: Austin
"""

import urllib.request as ur
import json

#sampledata
#json_url = 'http://py4e-data.dr-chuck.net/comments_42.json'

#realdata
json_url = 'http://py4e-data.dr-chuck.net/comments_363815.json'

data = ur.urlopen(json_url).read().decode('utf-8')
json_obj = json.loads(data)

sum = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])

print(sum)