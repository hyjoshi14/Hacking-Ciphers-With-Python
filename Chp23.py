## Finding Prime Numbers ##

## A prime number is an integer that is greater than 1 and has only two factors:
## 1 and itself. There are an infinite number of prime numbers and there is no 'largest'
## prime. They just keep getting bigger and bigger. The RSA Cipher makes use of very
## large prime numbers in the keys it uses. This makes it difficult to break a message
## coded by the RSA Cipher.

## Integers that are not prime are called composite numbers. They are divisible by 1, itself
## and atleast one more number. They are called prime numbers as they are made up of prime
## numbers multiplied together.

## Create helper functions related to prime numbers:
## isPrime - checks if a number is prime or not and returns a corresponding boolean values
## primeSieve - will use the 'Sieve of Eratosthenes' algorithm to generate prime numbers

import math, itertools, pprint, random

def my_isPrime(num):
	"""Checks if a number is prime or not"""
	if num < 2:
		return False
	else:
		factors = itertools.count(2)
		factors = itertools.takewhile(lambda x: x <= int(math.sqrt(num)), factors)
		for factor in factors:
			if divmod(num,factor)[-1] == 0:
				return False
		return True

def my_primeSieve(sieveSize):
	primes = set(range(2,sieveSize+1))
	for num in range(2,int(math.sqrt(sieveSize) + 1)):
		if num in primes:
			non_primes = filter(lambda x: x % num == 0, primes)
			non_primes = set(non_primes)
			primes = primes.difference(non_primes)
			primes.add(num)
	return primes

## The source code for Rabin Miller Algorithm has not been altered


def rabinMiller(num):
	s = num - 1
	t = 0
	while s % 2 == 0:
		s = s //2
		t += 1
	for trials in range(5):
		a = random.randrange(2, num - 1)
		v = pow(a, s, num)
		if v != 1:
			i = 0
			while v != (num-1):
				if i == t-1:
					return False
				else:
					i += 1
					v = (v ** 2) % num
	return True
	
def rabinMiller_isPrime(num):
	low_primes = my_primeSieve(1000)
	if num < 2:
		return False
	if num in low_primes:
		return True
	for prime in low_primes:
		if (num % prime) == 0:
			return False
	return rabinMiller(num)
	
	
def generateLargePrime(keysize = 1024):
	while True:
		num = random.randrange(2**(keysize-1),2**(keysize))
		if rabinMiller_isPrime(num):
			return num
	
		
if __name__ == "__main__":
	## Check is_prime function
	print my_isPrime(49)## Not Prime
	print my_isPrime(11)## Prime
	print my_isPrime(1)## Not Prime
	pprint.pprint(my_primeSieve(500*2))## low_primes
	print rabinMiller_isPrime(13)
	print rabinMiller_isPrime(45943208739848451)
	print generateLargePrime()
	