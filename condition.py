#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:18:17 2018

@author: lamkeatyee
"""

answer = input("Would you like express shipping?").lower()
shippingselected = False

if answer == "yes" :
    print ("That will be an extra $10")
    shippingselected = True
else:
    print("standard shipping selected..")
print ("Thank you")

if (shippingselected):
    print ("Thank you for selecting express shipping")