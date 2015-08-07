#!/usr/bin/env python

#Project Euler Problem 6
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


#Initialize all counters as zero.  
#theNumber will be our iterator.  squareSum will be the sum of all squares.
#sumToSquare will sum up all numbers, then be squared as sumSquare.
theNumber = 0
squareSum = 0
sumToSquare = 0
sumSquare = 0

#Do the appropriate math, then increment theNumber.
while theNumber <= 100:
    squareSum += theNumber * theNumber
    sumToSquare += theNumber
    theNumber += 1

#Make sure to square sumToSquare
sumSquare = sumToSquare * sumToSquare

#Print the difference
print sumSquare - squareSum
raw_input("Press enter to exit")
