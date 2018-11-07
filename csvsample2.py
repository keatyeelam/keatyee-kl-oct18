#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:29:06 2018

@author: lamkeatyee
"""

filename = "demo.csv"
accessmode = "r"


with open(filename,accessmode) as mycsvfile:
    datafromfile = csv.reader(mycsvfile)