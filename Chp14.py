##Chapter 14 - Modular Arithmetic With The Multiplicative and Affine Ciphers##

## In this script I shall attempt to recode a number of functions demonstrated 
## in this chapter using using various built-in Python libraries 
## (I shall not use "from library import *" in order to explicitly
## cite the library the method belongs to.)


import operator, fractions, string, itertools, copy

upper_case_letters = string.ascii_uppercase
lower_case_letters = string.ascii_lowercase
## Mod Operator - "Division Remainder" operator i.e. 21 mod 5 is 1, the remainder when 21 is divided by 5
## also -21 mod 5 is 4 not -1 as the result of a mod operation is never negative. Instead, -1 remainder is the same
## as 5-1 thus, the output of -21 mod 5 is 4 (5-1)

def my_mod(a,b):
	"""Obtain the remainder when a is divided by b"""
## if a is positive, while a is larger than or equal to b, decrease a by b
	if a > 0:
		while a >= b:
			a = operator.isub(a,b)
## else if a is negative, while a is negative, increase a by b
	else:
		while a < 0:
			a = operator.iadd(a,b)
	return a

	
#The Euclidean algorithm is a way to find the greatest common divisor of two positive integers, 
#a and b. First let me show the computations for a=210 and b=45.
#Divide 210 by 45, and get the result 4 with remainder 30, so 210=4·45+30.
#Divide 45 by 30, and get the result 1 with remainder 15, so 45=1·30+15.
#Divide 30 by 15, and get the result 2 with remainder 0, so 30=2·15+0.
#The greatest common divisor of 210 and 45 is 15.
def my_gcd(a,b):
	"""Obtain GCD of a and b using Euclid's Algorithm"""
	vals = [a,b]
	vals.sort(reverse = True)
	a,b = vals
	quot,rem = divmod(a,b)
	print '%d = %d*%d + %d' %(a,b,quot,rem)
	while rem != 0:
		print 'Divide by %d and %d' %(b,rem)
		a,b = b,rem
		quot,rem = divmod(a,b)
		print '%d = %d*%d + %d' %(a,b,quot,rem)
	print 'The greatest common divisor of %d and %d is %d' %(vals[0],vals[1],b)
	return b
## The GCD of two numbers can also be obtained using the gcd method in the fractions library.

	
## Two numbers a,b are relatively prime if their greatest common divisor is 1
def my_isrelativeprime(a,b):
	"""Check if two numbers are relatively prime"""
	if my_gcd(a,b) == 1:
		return True
	else:
		return False

## What would happen if multiplication were used to encrypt the characters for the Ceasar Cipher?
## Note: The Ceasar Cipher uses addition to encrypt messages in the plaintext to ciphertext
def my_CeasarMultKey(key):
	indices = range(26)
	indices2 = copy.deepcopy(indices) 
	indices2 = map(lambda x: x*key, indices2)
	indices2 = map(lambda x: my_mod(x,26), indices2)
	cipher_text = [upper_case_letters[index] for index in indices2]
	for (ptext_sym, num, enc, ctext_sym) in itertools.izip(upper_case_letters,indices,indices2,cipher_text):
		print 'Plaintext:%s, Number:%d , Encryption:%d, Ciphertext:%s ' %(ptext_sym, num, enc, ctext_sym)

## Problems with the Multiplicative Cipher		
## Two letters are mapped to the same cipher text
## A is always mapped to A		

## The Affine Cipher is a combination of the Ceasar Cipher and the Multiplicative Cipher
## It uses two keys namely "A" and "B". The indices are multiplied by "Key A", then modded by 26.
## Finally, they are increased by the value of "Key B". 
## Utilising these transformed indices, the ciphertext is obtained.

def my_AffineKey(key1,key2):
	if my_isrelativeprime(key1,26):
		indices = range(26) 
		indices = map(lambda x: x*key1, indices)
		indices = map(lambda x: my_mod(x,26), indices)
		indices = [my_mod(x+key2,26) for x in indices]
		cipher_text = [upper_case_letters[index] for index in indices]
		return ''.join(cipher_text)

## Instead of map, itertools.imap could also have been used, but the syntax for
## line 76 and 77 would change a little.
## e.g. line 76 would read indices = itertools.imap(lambda x: my_mod(x,26), [index for index in indices]) if
## line 75 were indices = itertools.imap(lambda x: x*key1, indices)
## This is because the object returned by itertools.imap is a itertools.imap object which would need to be
## unpacked using list comprehension.


## To decrypt text encoded in the Affine Cipher we would need the modular inverse of the key.
## A modular inverse (which we will call i) of two numbers (which we will call a and m) is such that (a * i) % m == 1.
		
def my_isModInverse(a,b):
	"""Obtain the modular inverse of a with respect to b"""
	for i in itertools.count():
		if (my_mod(a*i,b)) == 1:
			print '%d is the modular inverse of %d and %d' %(i,a,b)
			break
		else:
			print '%d is not the modular inverse of %d and %d' %(i,a,b)
			continue

if __name__ == "__main__":
	print my_mod(21,5)
	print my_mod(-21,5)
	print my_gcd(24,30)
	print my_gcd(409119243, 87780243)
	print fractions.gcd(24,30)
	print fractions.gcd(409119243, 87780243)
	my_CeasarMultKey(7)
	print my_AffineKey(7,20)
	my_isModInverse(7,26)
