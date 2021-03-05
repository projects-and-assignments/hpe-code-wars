import sys
import time
import os
from os import path,listdir
from os.path import isfile, join

# ------------------------------------------------------------------------
# CHANGE THIS BEFORE SUBMITTING!
AM_DEBUGGING = False
DATA_STUDENT = True
probID = 'prob06'
# ------------------------------------------------------------------------

'''
PROBLEM: Sir Isaac Newton is the deadliest person in space
DIFFICULTY LEVEL: Novice
TIME FOR PROBLEM AUTHOR TO CODE SOLUTION: 4 mins
ESTIMATED STUDENT COMPLETION TIME NEEDED: 5 mins
AUTHOR: Robert McAdams, mcadams@hpe.com, linkedin.com/in/RobertMcadams
LAST MODIFIED: 2021-02-22
WHAT IT TESTS: 
    1.) Ability to parse floating point decimals out of string data from a file
    2.) Ability to square numbers
    3.) Ability to take the square and cube root of numbers
    4.) Ability to understand and program solutions using programming concepts such as order of operations, keeping track of data, splitting a string, formatting output, implementing algorithms.
'''

# ========================================================================
def GetData(isDebug=False,filePath="input.txt"):
    'used to pull data from an input file, or standard in (depending on debug mode)'
    lines = []
    try:
        if (isDebug):
            myFile = open(filePath,"r")
            for line in myFile:
                #print(line.strip())
                lines.append(line.strip())
        else:
            for line in sys.stdin:
                #print(line.strip())
                lines.append(line.strip())
        return lines
    except:
        e = sys.exc_info()[0]
        print("bad things happened: "+str(e))
# ========================================================================
def Main(lines=[]):
    'Main Program'
    if (len(lines) > 0):
        for line in lines:
            if (line.strip() != '0'):
                # relevant info : P^2 == R^3
                # Given P, want R
                # Square P to get R^3
                # take cube root of R^3 to get R
                P = float(line.strip())
                P_Sqr = P**2 # now we have R^3
                R = format(round(P_Sqr**(1/3),4),'.4f') 
                print(R)
    else:
        print('** ERROR ** data file is malformed')

# ########################################################################
# ########################################################################
#                           MAIN PROGRAM
# ########################################################################
# ########################################################################

# Solutions I provide will be structured in this way, to allow quick-running
# all of the datasets (student and judge) -- as we use these solutions to
# generate the datasets ^_-
#
# That only will happen if debug mode is on. When reading from standard in
# this solution will always expect one (and only one) input file name/path.
#
# Student solutions would not be expected to be this in-depth. We would expect
# student solutions to simply look for the file to open :D

# ------------------------------------------------------------------------
# Display a warning to the Terminal if the solution is in Debug mode
if (AM_DEBUGGING):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n         WARNING WARNING WARNING               \n             DEBUG MODE IS ON!                 \n    DO NOT SUBMIT FOR JUDGING IN THIS MODE!    \n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    time.sleep(5)
# ------------------------------------------------------------------------
# GET THE DATA FROM THE DATA FILE(S)
DATASET = 'judge'
if (DATA_STUDENT):
    DATASET = 'student'
if (AM_DEBUGGING):
    files = [f for f in listdir(fr'{DATASET}_datasets\{probID}') if isfile(join(fr'{DATASET}_datasets\{probID}', f))]
    for file in files:
        if ('in.txt' in file):
            # print(f'{file}')
            lines = GetData(AM_DEBUGGING,fr'{DATASET}_datasets\{probID}\{file}')
            if (lines != None and len(lines) > 0):
                Main(lines)
            else:
                print('** ERROR ** data file was blank or missing')
else:
    lines = GetData(AM_DEBUGGING)
    if (lines != None and len(lines) > 0):
        Main(lines)
    else:
        print('** ERROR ** data file was blank or missing')
