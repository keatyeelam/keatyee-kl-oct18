#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:29:23 2018

@author: lamkeatyee
"""


guests = []

while name != "end":
    name = input("Please enter guest name: ")
    if name != "end":
        guests.append(name)

guests.sort()

for guest in guests:
    print (guest)