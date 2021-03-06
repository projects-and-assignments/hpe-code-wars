#!/usr/bin/env python

#CodeWars 2015
#
# Counting Cubes

# The input will be the mapping of names to their cube locations, a single name (no spaces) 
# followed by a single space and a cube location (1 to 300). 
# The first line of the input will list the number of name to cube mappings that we have. 
# If a cube is empty the name will be "NA". 
# If an employee does not have a cube assigned their cube location will be 0.
# 
# The output will consist of the number of empty cubes, 
# the number of duplicate cube assignments (two or more people assigned to the same cube), 
# and the number of unassigned cubes.
# 
# Sample Input
# 14
# Joe 123
# Bob 124
# Katy 125
# Sam 127
# Mike 126
# Lonely 124
# Fred 0
# Vivek 234
# Lars 236
# Oscar 237
# Caroline 123
# Erin 121
# Rachel 321
# Nate 227
# 
# Sample Output
# Empty Cubes: 1
# Duplicate Cube Assignments: 1
# Employees without Cube: 1


import sys

#globals
emptyCubes=0
duplicateCubes=0
withoutCubes=0

cubeAssignments = {'999':'None'} # an initial value to get started

lineCount = int(sys.stdin.readline().rstrip('\n'))
for i in range (1,lineCount+1):
    line = sys.stdin.readline()
    line = line.rstrip('\n')
    name, cubeString = line.split(None, 1)
    if (int(cubeString)==0):
        withoutCubes = withoutCubes+1  # Found an unassigned person
    elif (name == 'Lonely'):
        emptyCubes = emptyCubes+1      # Found an empty cube
    else:
        if (cubeString in cubeAssignments.keys()):
            duplicateCubes = duplicateCubes+1  # Found an already assigned cube (duplicate)
        else:
            cubeAssignments[cubeString]=name
# Finished, now print results
print("") # Empty line
print ("Lonely Cubes:", emptyCubes)
print ("Duplicate Cube Assignments:", duplicateCubes)
print ("Test Subjects without Cubes:", withoutCubes)
