#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:01:39 2018

@author: lamkeatyee
"""

#1. create a function to print hello

#def sayhello(firstname,lastname) :
#    print ("Hello " + firstname + " " + lastname + " there!!!")
#    return
#
##invoke the function
#sayhello("Mun Yeen","Chong")

var1 = input("Please enter your first number: ")

var2 = input("Please enter your second number: ")

def addtwo(var1,var2):
    sum = int(var1) + int(var2)
    return sum

print("Sum of " + var1 + " + " + var2 + " = " + str(addtwo(var1,var2)))