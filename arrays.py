#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:35:20 2018

@author: lamkeatyee
"""

guests = ['first','second','third']
#print(guests[1])

#print("First value is " + guests[0])

guests[0] = "Steve"

#print("First value now is " + guests[0])

guests.append('new guy')

#print("New value now is " + guests[-1])

#print("Second element now is " + guests[1])

#guests.remove('second')

#print("Second element after remove is " + guests[1])

#del guests[1]

#print("Second element now is " + guests[1])

#print(guests.index('third'))

#for steps in range (len(guests)):
#   print(guests[steps])

#scores = ['78','68','88','98','25']
#print(scores[-1])

#guests.sort
#
#for guest in guests:
#    print (guest)
#    
#print ("Done")

scores = ['78','68','88','98','25']

scores.sort()

for score in scores:
    print (score)
    
print ("Done")