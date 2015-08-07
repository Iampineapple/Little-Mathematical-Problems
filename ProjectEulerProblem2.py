#!/usr/bin/env python

#Project Euler Problem 2
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#Program accomplishes this by calculating Fibonacci numbers, in order, 
#until their value exceeds 4 million.  If a given Fibonacci number is even,
#it is added to the total.

maxNumber = 4000000

currentTerm = 1
previousTerm = 0
total = 0

while currentTerm < maxNumber:
    if currentTerm % 2 == 0:
        total = total + currentTerm
    tempOne = currentTerm
    tempTwo = previousTerm
    currentTerm = tempOne + tempTwo
    previousTerm = tempOne

print total
raw_input("Press enter to exit")
