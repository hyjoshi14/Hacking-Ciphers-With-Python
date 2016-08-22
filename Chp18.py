## Chapter 18 - Hacking the Simple Substitution Cipher ## 

## Implement a Map Reduce Job to obtain the word patterns for 
## the words present in our dictionary file

## As pointed out earlier, I would be focussing on built-in libraries,
## This part is an exception to the rule. A version of this code
## with an implementation using only the built-in libraries shall also
## be published


## We will use the MRJob library for this task

from mrjob.job import MRJob
from mrjob.step import MRStep
import collections
import pprint

## The Mapper takes as input a word in the dictionary file. For each word
## it removes the '\n' character and adds the unique letters along with their
## indices i.e. the position at which the letter first occurs into an OrderedDict.
## The OrderedDict preserves the order in which the elements are added to it.
## Using this dictionary, the transformed version of the word i.e. Word Pattern 
## is created.

## The Reducer groups all Words and Character Sets by their Word Pattern
## and returns a dictionary with the Word Pattern and the corresponding list of words and
## the number of words that have such a pattern

class WordPattern(MRJob):
	def mapper_1(self,_,word):
		word = word.replace('\n','')
		unique_letters = collections.OrderedDict()
		word_index = 0
		for char in word:
			if char not in unique_letters.keys():
				unique_letters[char] = word_index
				word_index += 1
		transformed_word = []
		for char in word:
			transformed_word.append(unique_letters[char])
		transformed_word = map(str,transformed_word)
		transformed_word = '.'.join(transformed_word)
		yield transformed_word,{"Word":word,"CharSet":unique_letters}
	
	def reducer_1(self,word_pat,words):
		list_of_words = []
		for word in words:
			list_of_words.append({word["Word"]:word["CharSet"]})
		yield {word_pat:list_of_words,"WordCount":len(list_of_words)},1
	
	# def mapper_2(self,key,data):
		# # if data['WordCount'] > 13000:
		# yield key,data
	
	# def reducer_2(self,key,data):
		# list_of_patterns = []
		# for word_pat_data in data:
			# list_of_patterns.append(word_pat_data)
		# pprint.pprint(sorted(list_of_patterns, key = lambda x: x['WordCount'], reverse = False)[:10])
		
	
	def steps(self):
		return[MRStep(mapper = self.mapper_1,
		reducer = self.reducer_1)]

## The command to run this MRJob job on the local system is similar to running any script i.e.
## one needs to be in the directory the script is located in i.e. '~' , the filename as 
## input (note: the complete file path would need to be provided if the file is not in '~') and
## an output directory separated by -o
## ~\Chp18.py EnglishDictionary.txt -o Output. The file shall be saved as part-0000. Open it and save it as
## a text file

word_patterns = []
def my_loadWordPatterns():
	

def my_GetWordPattern(word):
	word = word.replace('\n','')
	unique_letters = collections.OrderedDict()
	word_index = 0
	for char in word:
		if char not in unique_letters.keys():
			unique_letters[char] = word_index
			word_index += 1
	transformed_word = []
	for char in word:
		transformed_word.append(unique_letters[char])
		transformed_word = map(str,transformed_word)
		transformed_word = '.'.join(transformed_word)
	return transformed_word



if __name__ == "__main__":
	WordPattern.run()