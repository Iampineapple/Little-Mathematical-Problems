#!/usr/bin/env python
class Complex(object):
	#This is a simple implementation of complex arithmetic as a class
	#It was written in order to gain practice with Python classes
	#This class was written by Cory Haight-Nali on or around 2 August 2015
	
	def __init__(self, real, imaginary):
		#Create a complex number with real, and imaginary parts
		if(isinstance(real, (int, float, long))):
			self.real = real
		else:
			try:
				self.real = float(real)
			except ValueError:
				print "Real part is not a valid number"
			
		if(isinstance(imaginary, (int, float, long))):
			self.imaginary = imaginary
		else:
			try:
				self.imaginary = float(imaginary)
			except ValueError:
				print "Imaginary part is not a valid number"
	
	def display(self):
		#Print out the complex number in total
		if(self.imaginary == 0):
			print "Our complex number is ", self.real
		elif(self.imaginary > 0):
			print "Our complex number is ", self.real, " + ", self.imaginary, "i"
		else:
			print "Our complex number is ", self.real, " ", self.imaginary, "i"
	
	def __add__(self, second):
		#Addition operator between two numbers.  If second is complex, add them.
		#Otherwise, hope second is a real number and try to add it to the real part
		if(isinstance(second, Complex)):
			num = Complex(self.real + second.real, self.imaginary + second.imaginary)
			num.display()
			return num
		else:
			try:
				num = Complex(self.real + second, self.imaginary)
				num.display()
				return num
			except TypeError:
				print "That cannot be added !"
		
	def __sub__(self, second):
		#Subtraction operator between two numbers, self minus second.  
		#If second is complex, subtract them.  Otherwise, hope second is a real number,
		#and try to subtract it from the real part
		if(isinstance(second, Complex)):
			num = Complex(self.real - second.real, self.imaginary - second.imaginary)
			num.display()
			return num
		else:
			try:
				num = Complex(self.real - second, self.imaginary)
				num.display()
				return num
			except TypeError:
				print "Those cannot be subtracted !"
		
	def __mul__(self, second):
		#Multiplication operator between two numbers.  If second is complex, multiply them.
		#Otherwise, hope second is a real number, and try to multiply it against both parts 
		if(isinstance(second, Complex)):
			num = Complex(self.real * second.real - self.imaginary * second.imaginary, self.real * second.imaginary + self.imaginary * second.real)
			num.display()
			return num
		else:
			try:
				num = Complex(self.real * second, self.imaginary * second)
				num.display()
				return num
			except TypeError:
				print "Those cannot be multiplied !"
			
	def __div__(self, second):
		#Division operator between two numbers.  If second is complex,
		#divide them according to the algorithm for complex number division.
		#Otherwise, hope second is a real number, and just divide.
		
		if(isinstance(second, Complex)):
			#Create a complex conjugate of the denominator
			complexconjugate = Complex(second.real, -second.imaginary)
			
			#Multiply both numerator and denominator by the complex conjugate
			num = Complex(self.real * complexconjugate.real - self.imaginary * complexconjugate.imaginary, self.real * complexconjugate.imaginary + self.imaginary * complexconjugate.real)
			denom = Complex(second.real * complexconjugate.real - second.imaginary * complexconjugate.imaginary, second.real * complexconjugate.imaginary + second.imaginary * complexconjugate.real)
			
			#Divide and return
			ans = Complex(num.real / float(denom.real), num.imaginary / float(denom.real))
			ans.display()
			return ans
		else:
			try:
				num = Complex(self.real / float(second), self.imaginary / float(second))
				num.display()
				return num
			except TypeError:
				print "Those cannot be divided !"

				
	def __pow__(self, second):
		#Power between two numbers.  If second is complex, exponentiate them
		#by way of complicated math.  If it's not complex, 
		#make it a complex number, and call pow again
		
		if(isinstance(second, Complex)):
			import math
			first = (self.real**2 + self.imaginary**2)**(second.real/2.0) * math.exp(-second.imaginary * math.atan(float(self.imaginary)/self.real))
			inner = second.real * math.atan(float(self.imaginary)/self.real) + 0.5 * second.imaginary * math.log(self.real**2 + self.imaginary**2)
			second = Complex(math.cos(inner), math.sin(inner))
			ans = second * first #This also gets our number displayed
			return ans
		else:
			try:
				temp = Complex(second, 0)
				self ** temp
			except TypeError:
				print "Those cannot be exponentiated !"
	
		