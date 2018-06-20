# -*- coding: utf-8 -*-
"""
Created on 2018/6/20

@author: LeeJiangLee
"""
import urllib.request
response = urllib.request.urlopen('http://laomo.me/')
#result = response.read().decode('utf-8')
print(response.geturl())
print('\n')
print(response.getcode())
print('\n')
print(response.info())
#print(result)