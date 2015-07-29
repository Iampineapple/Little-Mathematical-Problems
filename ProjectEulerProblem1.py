#!/usr/bin/python

#Project Euler Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#Program does this by brute force checking each number below 1000, 
#and adding it to the total if it is divisible by 3 or 5


total = 0
belowNumber = 1000
currentNumber = 0

while currentNumber < belowNumber:
    total = total + currentNumber
    currentNumber += 3

currentNumber = 0

while currentNumber < belowNumber:
    if currentNumber % 3 != 0: 
        total = total + currentNumber
    currentNumber += 5

print total
raw_input("Press enter to exit")
