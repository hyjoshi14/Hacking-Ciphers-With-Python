## Chapter 11 - Detecting English Programmatically""

from __future__ import division ## Similar to operator.truediv
import string, collections, os
 

os.chdir(r'C:\Users\Dell\Desktop\GithubRepo\Hacking Ciphers With Python')

## To detect if a message is in english, we check the percentage of characters and also 
## the number of words in a message that are in english. An english dictionary and a string
## of english characters are required to achieve this.

## Create a string of characters
upper_case_letters = string.ascii_uppercase
letters_and_characters = ' '+upper_case_letters+upper_case_letters.lower()+'\t\n'
## Create an empty list to store the words in
words = []

messages = ["Robots are your friends. Except for RX-686. She will try to eat you.","&^%%hafybadf(())kkladfuan54","XXXXHello WorldXXXX",\
"***Hello World***"]
## Create a function to load the words from the dictionary into the empty list
def load_myDictionary():
	"""Load dictionary with 354986 English Words"""
	dictionary_file = open('EnglishDictionary.txt','r')
	for word in dictionary_file.readlines():
		words.append(word.replace('\n',''))
	print 'Dictionary has been loaded'
	print '\n'.join(words[:10])

def my_removeNonLetters(message):
	"""Removes characters not in the "letters_and_characters" object"""
	message = list(message)
	message = filter(lambda x: x in letters_and_characters, message)
	if len(message) == 0:
		return 0
	else:
		return ''.join(message)
	
def my_EngCount(message):
	"""Returns percentage of words in a message that are in English"""
	message = my_removeNonLetters(message)
	if message != 0:
		message = message.lower()
		message = message.split()
		word_count = collections.Counter()
		for word in message:
			if word in words:
				word_count.update([word])
		count = sum([val for val in word_count.values()])
		return count / len(message) * 100
	else:
		return 0
	
## Note: Default arguments here can be altered	
def my_isEng(message, wordPerc = 20, letterPerc = 85):
	"""Checks if a given message meets the threshold for wordPerc and letterPerc"""
	wordPerc_message = my_EngCount(message)
	cleaned_message = my_removeNonLetters(message)
	letterPerc_message = len(cleaned_message) / len(message) * 100
	if wordPerc_message >= wordPerc:
		if letterPerc_message >= letterPerc:
			print 'Message is in English.'
			print 'Word Percentage: %d & Letter Percentage: %d' %(wordPerc_message,letterPerc_message)
			return True
		else:
			print 'Message is not in English.'
			print 'Word Percentage: %d & Letter Percentage: %d' %(wordPerc_message,letterPerc_message)
			return False
	else:
		print 'Message is not in English.'
		print 'Word Percentage: %d & Letter Percentage: %d' %(wordPerc_message,letterPerc_message)
		return False
	


	
if __name__ == "__main__":
	print os.listdir(os.getcwd())
	load_myDictionary()## All words are in lower case
	print my_removeNonLetters("ABCF23492)))(13123*&^")
	for message in messages:
		print 
		print message
		print my_EngCount(message)
		print my_removeNonLetters(message)
		print my_isEng(message, letterPerc = 60)
		print 
