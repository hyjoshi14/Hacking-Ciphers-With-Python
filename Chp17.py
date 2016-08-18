## Chapter 17 - The Simple Substitution Cipher ##

## To implement the simple substitution cipher, choose a random letter to encrypt 
## each letter of the alphabet. Use each letter once and only once. This cipher can have
## 403,291,461,126,605,635,584,000,000 possible orderings for keys. Making it difficult
## for a computer to brute-force through them.

import string, random, collections

upper_case_letters = string.ascii_uppercase
lower_case_letters = upper_case_letters.lower()
## For a key to be valid in a substitution cipher, every letter must appear and it 
## should appear exactly once.

message = """If a man is offered a fact which goes against his instincts, he will scrutinize
 it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the 
 other hand, he is offered something which affords a reason for acting in accordance to 
his instincts, he will accept it even on the slightest evidence. The origin of myths is explained
 in this way. -Bertrand Russell"""

def my_isValidKey(key):
	"""Takes as input a string for the key of the substitution cipher and checks if it is valid."""
	print 'Key:%s' %key
	letter_count = collections.Counter(key.upper())
	unique_letters = [letter for letter,count in letter_count.items() if count == 1]
	duplicate_letters = [letter for letter,count in letter_count.items() if count > 1]
	unique_letters_set = set(unique_letters)
	if len(unique_letters)  == len(upper_case_letters):
		if len(duplicate_letters) == 0:
			if len(unique_letters_set.difference(set(upper_case_letters))) == 0:
				print 'This is a valid key'
				return True
			else:
				print 'This is not a valid key'
				return False
		else:
			print 'This is not a valid key'
			return False
	else:
		print 'This is not a valid key'
		return False


def my_GetKey():
	"""Generates a valid key for the Substitution Cipher."""
	key = list(upper_case_letters)
	random.shuffle(key)
	return ''.join(key)
		
def my_SubCipher(message, key, mode = "e"):
	"""Encrypts / Decrypts a message with a valid key using the Substituion Cipher."""
	if my_isValidKey(key):
		if mode == "e":
			upper_table = string.maketrans(upper_case_letters,key.upper())
			lower_table = string.maketrans(lower_case_letters,key.lower())
		elif mode == "d":
			upper_table = string.maketrans(key.upper(),upper_case_letters)
			lower_table = string.maketrans(key.lower(),lower_case_letters)
		else:
			print 'Mode can only be "e" (Encrypt) or "d" (Decrypt)'
			return None
		message = message.translate(upper_table).translate(lower_table)
		return message

		
		
if __name__ == "__main__":
	print my_isValidKey(upper_case_letters)## Valid
	print 
	print my_isValidKey(lower_case_letters)## Valid
	print 
	print my_isValidKey("ABCDEF:JKLSDUDUVDUUIMMMM")## Invalid
	print 
	key = my_GetKey()
	print 'Encrypting Message'
	encrypted_message = my_SubCipher(message,key)
	print encrypted_message
	print 
	print 'Decrypting Message'
	decrypted_message = my_SubCipher(encrypted_message,key, mode = "d")
	print decrypted_message