#!/user/bin/env python

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?
#
#Script written by Cory Haight-Nali on or around 3 August 2015

import math

primeList = [2]
n = 3

#Sieve of Eratosthenes to make a primeList of primes
#until we have the 10,001th prime
while(len(primeList) < 10001):
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
	
print "The 10001th prime is ", primeList[10000]
raw_input("Press any key to exit")
