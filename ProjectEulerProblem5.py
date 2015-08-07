#!/usr/bin/env python

#Project Euler Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#Given a list of numbers, ensure that no number in the list is a multiple of another
def no_multiples(multipleList):
    for n in multipleList:
        for m in multipleList:
            if n % m == 0 and n != m:
                multipleList.remove(m)
    return multipleList




maxDivisor = int(raw_input("Output: a number divisible by all numbers\
 1 to input \n"))
theNumber = maxDivisor
modSum = 73

#Create a list of numbers, 1 to 20
i = 1
divisors = []
while i <= maxDivisor:
    divisors.append(i)
    i += 1

#Remove all multiples in the list
no_multiples(divisors)

#theNumber is the number to test if it is divisible by all the numbers 1 to maxDivisor
#We increment theNumber by maxDivisor each iteration
while modSum != 0:
    theNumber += maxDivisor
    modSum = 0
	#Sum up all the remainders of theNumber mod items in divisors.  If it's zero, break, 
	#as we've found a number divisible by all the numbers 1 to maxDivisor.
    for item in divisors:
        modSum += theNumber % item
        if modSum !=0:
            break
    
print theNumber
raw_input("Press enter to exit")



