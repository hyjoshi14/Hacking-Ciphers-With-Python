## Chapter 20 - Frequency Analysis ##

## There are 26 letters in the English alphabet, each of them occur with 
## differing frequencies in English text. Some letters are used more than others.
## E, T, A and O very frequently, in contrast, J, X, Q and Z are rarely found in 
## English text. Using this bit of information the Vigenere Cipher i.e. The Undecipherable
## Cipher can be cracked. This technique can be labelled Frequency Analysis. The word 'ETAOIN'
## is a useful mnemonic to remember the six most frequent letters. Similarly 'VKJXQZ' is a string
## containing the six least frequent letters. 

## The counting of letters and how frequently they occur in both plaintexts and ciphertexts is called
## frequency analysis. Since the Vigenere Cipher is essentially multiple Ceasar cipher keys used in 
## the same message, using frequency analysis each subkey can be hacked one at a time based on the 
## letter frequency of each subkey's decrypted text. By simply ordering the letters in our ciphertext 
## from most frequent to least frequent a Frequency Match Score will be calculated for this order of
## frequencies.

## The frequency match score is calculated in the following manner:
## Initially the score is set to 0, for every letter in 'ETAOIN' appearing among the six
## most frequent letters the score is increased by one. This approach is replicated for
## the presence of 'VKJXQZ' in the six least frequent letters of the frequency ordering.
## Thus the Frequency Match Score ranges from 0(Completely unlike regular English) to 12 (
## identical to regular English's letter frequency).


import collections, string, operator, pprint

upper_case_letters = string.ascii_uppercase
top_6 = 'ETAOIN'
bottom_6 = 'VKJXQZ'

test_message = """Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza 
sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia 
pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, 
ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. 
-Facjclxo Ctrramm"""

## To perform frequency analysis, three functions that will prove to be helpful are:
## 1.getLetterCount() - Takes a message and returns a dictionary that has the count each letter in the message
## 2.getFrequencyOrder() - Takes a message and returns a string of the 26 letters ordered in descending order of frequency
## 3.englishFreqMatchScore() - Takes a message and returns an integer from 0 to 12 indicating the message's letter frequency match score

## Using a Counter ishelpful in this scenario, it automatically stores values in descending order.

def my_getLetterCount(message):
	"""Takes a message and returns a dictionary that has the count each letter in the message."""
	counter = collections.Counter()
	for char in message:
		if char.upper() in upper_case_letters:
			counter.update(char.upper())
	return counter
	
def my_getFrequencyOrder(message):
	"""Takes a message and returns a string of the 26 letters ordered in descending order of frequency."""
	counts = my_getLetterCount(message)
	counts = sorted(counts, key = lambda x: counts[x], reverse = True)
	return ''.join(counts)
	
def my_englishFreqMatchScore(message):
	"""Takes a message and returns an integer from 0 to 12 indicating the message's letter frequency match score."""
	sorted_string = my_getFrequencyOrder(message)
	match_score = 0
	for char in sorted_string[:6]:
		if char in top_6:
			match_score = operator.iadd(match_score, 1)
	for char in sorted_string[-6:]:
		if char in bottom_6:
			match_score = operator.iadd(match_score, 1)
	return match_score
	

if __name__ == "__main__":
	print 'Letter Count'
	pprint.pprint(my_getLetterCount(test_message))
	print 
	print 'Frequency Order'
	pprint.pprint(my_getFrequencyOrder(test_message))
	print 
	print 'Match Score'
	pprint.pprint(my_englishFreqMatchScore(test_message))
