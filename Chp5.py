## Chapter 5 - The Reverse Cipher##

## The Reverse Cipher encrypts a message by printing it in reverse order.
## Below code helps accomplish the same. It takes as input the message.
## Then, it converts the message to a list and arranges it in reverse.
## Using the join method for strings the reversed message is generated.

def my_RevCipher(plaintext):
	"""Encode a message using the reverse cipher"""
	out = list(plaintext)
	out = out[::-1]
	out = ''.join(out)
	return out
	
	
if __name__ == "__main__":
	print my_RevCipher("Hello World!")
	print my_RevCipher("Three can keep a secret, if two of them are dead.")