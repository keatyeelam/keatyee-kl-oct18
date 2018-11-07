#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:42:21 2018

@author: lamkeatyee
"""

import datetime

birthday = input ("What is your birthday? (dd/mm/yyyy):")

birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()

print ("Your birth month is " + birthdate.strftime('%B'))

currentdate = datetime.date.today()
print (birthdate - currentdate)

