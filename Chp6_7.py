## Chapter 6 - The Ceasar Cipher ##
## Chapter 7 - Hacking the Ceasar Cipher with the Brute Force Technique  ##

## The Ceasar Cipher uses keys which are integers from 0 to 25
## to encrypt a message. So, even if a cryptanalyst knows that the
## message was encrypted using the Ceasar Cipher, he/she would also 
## need to know the key to be able to decrypt it.


## I'll attempt to recreate the Ceasar Cipher using several different
## methods and libraries available in Python
import string, collections, random, itertools
upper_case_letters = string.ascii_uppercase
lower_case_letters = upper_case_letters.lower()
message = "This is my secret message."

def my_CeasarCipher(message, key, mode = "e"):
	upper_case_deque = collections.deque(upper_case_letters)
	lower_case_deque = collections.deque(lower_case_letters)
	upper_case_deque.rotate(key)
	lower_case_deque.rotate(key)
	if mode == "e":
		upper_translate_table = string.maketrans(upper_case_letters,''.join(upper_case_deque))
		lower_translate_table = string.maketrans(lower_case_letters,''.join(lower_case_deque))
		message = message.translate(upper_translate_table)
		return message.translate(lower_translate_table)
	if mode == "d":
		upper_translate_table = string.maketrans(''.join(upper_case_deque),upper_case_letters)
		lower_translate_table = string.maketrans(''.join(lower_case_deque),lower_case_letters)
		message = message.translate(upper_translate_table)
		return message.translate(lower_translate_table)
	if mode != "e" or mode != "d":
		print 'Mode can only be "e" (Encrypt) or "d" (Decrypt)'
		

		
if __name__ == "__main__":
	## Encrypt
	key = random.randint(0,25)
	print 'Encrypting: %s with Key: %d' %(message,key)
	print my_CeasarCipher("This is my secret message.", key)
	encrypt_message = my_CeasarCipher("This is my secret message.", key)
	## Decrypt
	print 'Decrypting: %s with Key: %d' %(encrypt_message,key)
	print my_CeasarCipher(encrypt_message, key, mode = "d")
	#print 'Check if error message will be printed for mode.'
	#print my_CeasarCipher(encrypt_message, key, mode = "r")
	## Decrypt using brute force
	print 'Decrypting: "%s" using brute force' %(encrypt_message)
	possible_keys = itertools.islice(itertools.count(),26)
	for key in possible_keys:
		print "Key#%d: %s" %(key,my_CeasarCipher(encrypt_message,key,mode = "d"))