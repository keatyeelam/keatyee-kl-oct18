#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:17:17 2018

@author: lamkeatyee
"""

import csv

mycsvfile = open ('demo.csv','r')
datafromfile = csv.reader(mycsvfile)

print(datafromfile)

for row in datafromfile:
#    print(row)
#    for values in row:
#        print(values + "\n")
    print(','.join(row))
    
mycsvfile.close()