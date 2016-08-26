## Chapter 21 - Hacking the Vigenere Cipher##

import collections, re, pprint, operator, string

## I have not included a code here to hack the Vigener Cipher. Codes to support
## the relevant concepts have been listed and also functions required from other 
## modules are available in the repository.



letters = string.ascii_uppercase
NUM_MOST_FREQ_LETTERS = 4
test_message = """hyjafhsjfbshyjafidybgfshyjaifhfgbhyjaidfbifgyshyjafnsfgneahyj"""
MAX_KEY_LENGTH = 16
NONLETTERS_PATTERN = re.compile(r'[^a-z]', re.MULTILINE|re.IGNORECASE)

def my_getSeqs(message,seq_size = range(3,6)):
	"""Splits a message into ngrams of the desired size and also counts their occurences."""
	message = NONLETTERS_PATTERN.sub('',message)
	list_of_seqs = collections.Counter()
	for n in seq_size:
		for i in range(len(message)-n+1):
			list_of_seqs.update([message[i:i+n]])
	return list_of_seqs
	
def my_getSeqSpacing(message,list_of_seqs, n = 100):
	"""Obtains the distance between two occcurences of a sequence for the 'n' most common sequences."""
	message = NONLETTERS_PATTERN.sub('',message)
	if isinstance(list_of_seqs,collections.Counter):
		most_common_seqs = list_of_seqs.most_common(n)
		seqSpace_dict = {}
		for seq,count in most_common_seqs:
			seqSpace_dict[seq] = []
			seq_compiler = re.compile(seq,re.MULTILINE|re.IGNORECASE)
			all_occurences = seq_compiler.finditer(message)
			for match_object in all_occurences:
				seqSpace_dict[seq].append(match_object.start())
			seqSpace_dict[seq] = list(set(map(lambda x,y: x-y, seqSpace_dict[seq][1:],seqSpace_dict[seq][:-1])))
		return seqSpace_dict
	else:
		print 'Ensure list of sequences is a "collections.Counter" object'
		return None
	
def my_getUsefulFactors(num):
	"""Obtains the factors of a number (excluding one) upto the specfied maximum key length."""
	if num > 2:
		factors = []
		for i in range(2,MAX_KEY_LENGTH+1):
			if operator.mod(num,i)== 0:
				factors.append(i)
				factors.append(operator.div(num,i))
		factors = filter(lambda x: x!=1, factors)
		return list(set(factors))
	else:
		return [None]
		
def my_getMostFreqFactors(seqSpace_dict, n = 3):
	"""Gets the most frequent 'n' factors for the sequence lengths."""
	most_freq_factors = collections.Counter()
	for key,lengths in seqSpace_dict.items():
		if len(lengths) != 0:
			factors = map(my_getUsefulFactors,lengths)
			factors = reduce(lambda x,y: x + y, factors)
			for factor in factors:
				most_freq_factors.update([factor])
	return most_freq_factors.most_common(n)

def my_kasiskiAlgorithm(message):
	""" Performs the Kasiski Examination on a message and returns the likely keys for a message."""
	seqs = my_getSeqs(message)
	rep_seqs = my_getSeqSpacing(message,seqs)
	freqFactors = my_getMostFreqFactors(rep_seqs, n = 1000)
	all_likely_keys = [factor for factor,count in freqFactors]
	return all_likely_keys

def return_list():
	"""A helper function that shall return a list."""
	return []
	
def my_getSubkeyLetters(n, keylength, message):
	"""Utilises default dictionary to provide the nth subkey letters for a message."""
	message = NONLETTERS_PATTERN.sub('',message)
	message_dict = collections.defaultdict(return_list)
	for i in range(len(message)):
		list_index = divmod(i,keylength)[-1] + 1
		message_dict[list_index].append(message[i])
	print message_dict
	if n in message_dict.keys():
		return ''.join(message_dict[n])
		
	

if __name__ == "__main__":
	seqs = my_getSeqs(test_message)
	print seqs
	print 
	print
	seq_dict = my_getSeqSpacing(test_message,seqs)
	pprint.pprint(seq_dict)
	print
	print
	print my_getUsefulFactors(16)
	pprint.pprint(my_getMostFreqFactors(seq_dict, n = 5))
	print
	print my_kasiskiAlgorithm(test_message)
	print 
	print my_getSubkeyLetters(3,3,test_message)