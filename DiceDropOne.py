#!/usr/bin/env python
#made by Cory on 18 Aug 2014
#This program will take ndp (as in, n dice with p sides on each die)
#and calculates the average of ndp, drop the lowest
#We do this by summing up all the possible die combinations,
#and then dividing by the number of die combinations



#This function checks if we've incremented a die's value beyond the possible values
#If so, it sets the die back to one, increments the next die, and checks if that
#die's value has gone beyond the possible values
def checkforoverflow(array, index, p):
    if array[index] > p:
        array[index] = 1
        array[index+1] +=1
        checkforoverflow(array, index+1, p)
    return


import math

#Ask the user for some input, set indexarray as our array of dice, 
#and set the total to zero.  Indexarray contains one more entry than the number of dice-
#when the final item is incremented to two, we've gone through all the permutations
print "Let's calculate the average of ndp, drop the lowest !"
n = int(raw_input('What is n ? (How many dice do we have ?)'))
p = int(raw_input('What is p ? (How many sides does each die have ?'))
indexarray = [1]*(n+1)
averagetotal = 0


#Check all the permutations, adding their value to averagetotal, and checking for overflow
while indexarray[n] < 2:
    averagetotal += sum(indexarray[0:n]) - min(indexarray[0:n])
    indexarray[0] += 1
    checkforoverflow(indexarray, 0, p)

average = averagetotal / float(p**n)
print "The average was ", average
