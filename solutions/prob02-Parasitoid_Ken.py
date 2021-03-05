#!/usr/bin/env python

#CodeWars 2015
#
#Parasitoid

# Write a program that uses Thompson's model to predict the rate of parasitism for a pair of input values.
# Input
# The first line of input is the value of C, the Mean Female Egg Compliment, an integer between 1 and 10,000. 
# The second line is the value of P, the Number of Females Searching, an integer between 1 and 100,000. 
# 1300
# 97450
# Output
# The program must print the value of Pe, the Number of Eggs Laid. 
# The answer must match the judge's expected value precisely.
#   126685000

import sys

#print ("Enter P and C each on its own line. ")
P = int(sys.stdin.readline())
C = int(sys.stdin.readline())
print (P*C)
