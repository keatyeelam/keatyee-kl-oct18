#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:07:46 2018

@author: lamkeatyee
"""

import datetime

currenttime = datetime.datetime.now()

print (currenttime)
print (currenttime.hour)
print (currenttime.minute)
print (currenttime.second)

print (datetime.datetime.strftime(currenttime,'%H:%M'))
print (datetime.datetime.strftime(currenttime,'%I:%M %p'))