## Chapter 8 - The Transposition Cipher, Encrypting ##
## Chapter 9 - The Transposition Cipher, Decrypting ##

## Instead of replacing characters with other characters, the transposition cipher jumbles up 
## the message into an order that makes it unreadable.

## It works as follows:
### 1.Count the number of characters in the message and the key.
### 2.Draw a number of boxes equal to the key in a single row. (For example, 12 boxes for a key of 12.)
### 3.Start filling in the boxes from left to right, with one character per box.
### 4.When you run out of boxes and still have characters left, add another row of boxes.
### 5.Shade in the unused boxes in the last row.
### 6.Starting from the top left and going down, write out the characters. When you get to the bottom of the column, 
### move to the next column to the right. Skip any shaded boxes. This will be the ciphertext.

## Lets understand the grid structure
## For a given message and key, this code shall split the message up 
## into equal lists of the size of the key. It shall return a list of lists
## in which each list is a row corresponding to the grid for encryption
import operator, math, random

message = "Common sense is not so common. Give me a Hell Yeah!!"

def my_GridStructure(message,key):
	"""Create a grid of the message to be encrypted."""
	message = list(message)
	grid = []
	while len(message) != 0:
		row = message[:key]
		if len(row) != key:
			row = row + [' ']*(key - len(row))## Append spaces to the end of rows which are not equal in length to the key
		grid.append(row)
		del message[:key]
	return grid

## Once the grid structure is in place, encryption can begin according to
## step 6. Since all the rows in the grid are the same size, by obtaining
## the length of one such row, the key is obtained. Then, for each row
## if the corresponding element is combined and merged together, the 
## ciphertext shall be in place.

def my_EncryptGrid(grid):
	"""Traverse through the grid and combine characters ocuring in a column."""
	key = len(grid[0])
	message = ''
	for i in range(key):
		transposed_message = ''.join([row[i] for row in grid])
		message = operator.iadd(message,transposed_message)
	return message

## Collapse these functions into one to perform encryptino according to the 
## Transposition Cipher

def my_TranspoCipherV1(message,key):
	"""Encrypt a message using the Transpose Cipher."""
	grid = my_GridStructure(message,key)
	transposed_message = my_EncryptGrid(grid)
	return transposed_message.strip()

## Decrytping a message encoded using the Transposition Cipher involves the same tasks as above
## after transposing the original grid that was used to encrypt the message
## If the length of the message is known and the key is known, the number of columns in the grid
## is equal to the size of the grid divided by the key (Note: Key = No.of Columns and No.of Cells in
## a matrix = No.of Columns * No.of Rows). It should also be noted that not all message lengths are
## completely divisible by the key. But, the code that creates the grid ensures every row is of equal size.
## Therefore by using the ceiling of the result obtained by dividing the Length of the Message and Key
## the number of rows is obtained which can in turn be used as the number of columns to decrypt the message.

## Adjusting the my_TranspoCipherV1 version to also decrypt a message
def my_TranspoCipherV2(message,key, mode = "e"):
	"""Manipulate a message using the Transpose Cipher. Modes can be specified"""
	if mode == "e":
		out = my_TranspoCipherV1(message,key)
		return out
	if mode == "d":
		decryption_key = math.ceil(operator.truediv(len(message),key)) ## Returns a float 
		decryption_key = int(decryption_key) ## Slice indices must be integers not float
		out = my_TranspoCipherV1(message,decryption_key)
		return out
	if mode != "e" or mode != "d":
		print 'Mode can only be "e" (Encrypt) or "d" (Decrypt)'
		
if __name__ == "__main__":
	## Understanding the grid structure
	grid_example = (my_GridStructure(message,8))
	for row in grid_example:
		print row
	## Encrypting the message
	print my_EncryptGrid(grid_example)
	print my_TranspoCipherV1(message,25)
	print 'Understanding the logic for decrypting the Transposition Cipher'
	print 'Message:%s' %(message)
	print 'Length Message: %d'%(len(message))
	print 'Encryption Key: %d' %8
	print 'Grid Structure'
	for row in grid_example:
		print row
	print 'No.Of Rows: %d' %(math.ceil(operator.truediv(len(message),8)))
	print 'Encrypting message: %s' %message
	## Checking Decryption program
	for i in range(10):
		print '*' * 50
		key = random.randint(1,len(message)/2)
		print 'Key:%d' %key
		encrypted_message = my_TranspoCipherV2(message,key)
		print 'Encrypted Message:%s' %encrypted_message
		print 'Decrypting Message'
		decrypted_message = my_TranspoCipherV2(encrypted_message,key, mode = "d")
		print 'Decrypted Message:%s' %decrypted_message
		print '*' * 50