## Chapter 19 - The Vigenere Cipher ##

## The Vigenere Cipher has too many possible keys to brute-force through.
## It is one of the stronger ciphers compared to the ones seen earlier.
## Until Charles Babbage broke it in the 19th century, it was called "The Undecipherable Cipher"

## It is similar to the Ceasar Cipher, except it uses multiple keys. Because it uses more than one
## set of substitutions it is called a polyalphabetic substitution cipher. A letter key is used instead of a numeric one.
## 	The key is a series of letters. This single key is split into many subkeys. The first subkey encrypts the first letter
## the second subkey the second and so on. The subkey is used in this cyclical manner until all characters in the message are encrypted.

import string, collections, itertools, timeit

message = "Common sense is not so common."
subkey = "PIZZA"
upper_case_letters = string.ascii_uppercase
lower_case_letters = string.ascii_lowercase

test_message = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist. 
e was highly influential in the development of computer science, providing a formalisation of the concepts of "algorithm" 
and "computation" with the Turing machine. Turing is widely considered to be the father of computer science and artificial 
intelligence. During World War II, Turing worked for the Government Code and Cypher School (GCCS) at Bletchley Park, 
Britain's codebreaking centre. For a time he was head of Hut 8, the section responsible for German naval cryptanalysis. 
He devised a number of techniques for breaking German ciphers, including the method of the bombe, an electromechanical 
machine that could find settings for the Enigma machine. After the war he worked at the National Physical Laboratory, 
where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's 
Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers and 
became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted 
oscillating chemical reactions such as the Belousov-Zhabotinsky reaction, which were first observed in the 1960s. 
Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the 
United Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing 
died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that his 
death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an 
Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of the British government 
for "the appalling way he was treated." As of May 2012 a private member's bill was before the House of Lords which would grant 
Turing a statutory pardon if enacted."""

test_key = "ASIMOV"
## Understand the logic of the Vigenere Cipher
def my_printSubkey(message,key):
	"""Returns a string indicating which character in the key shall encode/decode a message."""
	indices = itertools.cycle(range(len(key)))
	subkey_encrypt = ''
	for char in message:
		if char in upper_case_letters or char in lower_case_letters:
			subkey_encrypt += key[indices.next()]
		else:
			subkey_encrypt += char
	print message
	print subkey_encrypt

def get_Subkey(message,key):
	"""Provides a list of message character and subkey pairs to encode/decode a character in a message."""
	indices = itertools.cycle(range(len(key)))
	subkey = []
	for char in message:
		if char in upper_case_letters:
			subkey.append(key[indices.next()].upper())
		elif char in lower_case_letters:
			subkey.append(key[indices.next()].lower())
		else:
			subkey.append(char)
	return zip(list(message),subkey)

def my_VigCipher(message,key,mode = "e"):
	"""Encodes/decodes a message using the logic of the Vigenere Cipher."""
	upper_case_table = collections.deque(upper_case_letters)
	lower_case_table = collections.deque(lower_case_letters)
	out = ''
	if mode == "e":
		subkeys = get_Subkey(message,key)
		for char,subkey in subkeys:
			if char in upper_case_letters:
				upper_case_table.rotate(26 - upper_case_letters.find(subkey.upper()))
				out += upper_case_table[upper_case_letters.find(char)]
				upper_case_table.rotate(upper_case_letters.find(subkey.upper()))
			elif char in lower_case_letters:
				lower_case_table.rotate(26 - lower_case_letters.find(subkey.lower()))
				out += lower_case_table[lower_case_letters.find(char)]
				lower_case_table.rotate(lower_case_letters.find(subkey.lower()))
			else:
				out += char
		return out
	if mode == "d":
		subkeys = get_Subkey(message,key)
		for char,subkey in subkeys:
			if char in upper_case_letters:
				upper_case_table.rotate(26 - upper_case_letters.find(subkey.upper()))
				out += upper_case_letters[''.join(upper_case_table).find(char)]
				upper_case_table.rotate(upper_case_letters.find(subkey.upper()))
			elif char in lower_case_letters:	
				lower_case_table.rotate(26 - lower_case_letters.find(subkey.lower()))
				out += lower_case_letters[''.join(lower_case_table).find(char)]
				lower_case_table.rotate(lower_case_letters.find(subkey.lower()))
			else:
				out += char
		return out
	else:
		print "Mode can only be 'e' (Encrypt) or 'd' (Decrypt)"
		
def my_timeVigCipher():
		my_VigCipher(test_message,test_key, mode = "d")
	
if __name__ == "__main__":
	my_printSubkey(message,subkey)
	print get_Subkey(message,subkey)
	print
	print 'Encrypting'
	encrypted_message = my_VigCipher(test_message,test_key)
	print encrypted_message
	print 
	print 'Decrypting'
	decrypted_message = my_VigCipher(encrypted_message,test_key,mode = "d")
	print decrypted_message
	print 'Testing'
	print decrypted_message == test_message
	print 'Timing 10000 runs'
	print timeit.timeit(my_timeVigCipher, number = 10000)