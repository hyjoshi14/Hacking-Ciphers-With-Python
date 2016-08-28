## Chapter 10 - Programming a program to test our program ##

## To check if the programs for the ciphers are encrypting and decrypting the messages properly,
## different messages can be generated and different keys can be set for each message. Instead of
## typing these different messages and keys, a computer program that generates a random message,
## sets an arbitrary key and returns to the user output which informs whether the plaintext and
## the ciphertext corrrespond to each other. Such a program can check if the encryption and
## decryption programs fro a cipher work. This is called automated testing.

## This file shall only contain the code to generate random strings of messages for testing and providing
## an arbitrary key for encrypting and decrypting the message. 

import string, random

upper_case_letters = string.ascii_uppercase
lower_case_letters = string.ascii_lowercase

def my_getRandomMessage():
	"""Generates a random message using english alphabets."""
	complete_letters = upper_case_letters + lower_case_letters
	complete_letters = list(complete_letters)
	random.shuffle(complete_letters)
	complete_letters = complete_letters * random.randint(4,40)
	random.shuffle(complete_letters)
	complete_letters = ''.join(complete_letters)
	return complete_letters[:random.randint(10,len(complete_letters))]
	
def my_getRandomKey(message,encryption_type = "ceasar"):
	"""Returns an arbitrary key to encode a message. Encryption Type takes as arguments 'ceasar' and 'transposition'."""
	if encryption_type == "ceasar":
		return random.randint(1,25)
	elif encryption_type == "transposition":
		return random.randint(1,len(message)/2)

		
if __name__ == "__main__":
	## Messages for Ceasar Cipher
	for i in range(10):
		message = my_getRandomMessage()
		key = my_getRandomKey(message)
		print "Random Message: %s" %message
		print "Ranodm Key: %d" %key
	
	## Messages for Transposition Cipher
	for i in range(10):
		message = my_getRandomMessage()
		key = my_getRandomKey(message,'transposition')
		print "Random Message: %s" %message
		print "Ranodm Key: %d" %key