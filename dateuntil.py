#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:10:37 2018

@author: lamkeatyee
"""

import datetime

currentdate = datetime.date.today()
print (currentdate)
print (currentdate.year)
print (currentdate.month)
print (currentdate.day)

print (currentdate.strftime('%A, %d %B %Y'))