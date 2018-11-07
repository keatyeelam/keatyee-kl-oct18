#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:36:44 2018

@author: lamkeatyee
"""

filename = "sample.txt"
accessmode = "w"

myfile = open(filename,accessmode)
myfile.write("Hi!!,\n")
myfile.write("How are you?")
myfile.close()
