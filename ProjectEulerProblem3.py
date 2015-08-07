#!/usr/bin/env python

#Project Euler Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
#
#Script written by Cory Haight-Nali on or around 3 August 2015

import math

#Get the number we're looking for the largest prime factor of.
#Seed the list of Primes with the number 2, and look at 3 as the
#first number we'll test for primeality
maxnum = int(raw_input("Input # to find the largest prime factor of \n"))
primeList = [2]
n = 3
sqrtmax = math.sqrt(maxnum)

#Sieve of Eratosthenes to make primeList a list of primes
#up to and including sqrt(maxnum)
while(n < sqrtmax):
    i = 0
    nPrime = True
    while(i < len(primeList) and primeList[i] <= math.sqrt(n)):
        if(n % primeList[i] == 0):
            nPrime = False
            break
        i += 1
    if(nPrime == True):
                primeList.append(n)
    n += 1

#Now, use the list of primes to find the largest prime factor
#and print the resulting largest prime factor
largestPrimeDivisor = 1
for item in primeList:
        if(maxnum % item == 0):
                largestPrimeDivisor = item

print "The largest prime divisor is ", largestPrimeDivisor
