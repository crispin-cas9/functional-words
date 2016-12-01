# Shakespeare analysis using functional words

import re
import urllib2
from pprint import pprint

# fword = functional word

fwords = urllib2.urlopen("https://fling.seas.upenn.edu/~maeisen/wiki/functionwords.txt").read().split(" ")

# shakespeare = urllib2.urlopen("http://cs.stanford.edu/people/karpathy/char-rnn/shakespeare_input.txt").read().lower()

data = open("test2.txt").read().lower()
prologue = re.findall(r"[^.;:!?]+", data)
prologue = [re.findall(r"[\w']+", item) for item in prologue]

indices = []

for sentence in prologue:
	sdict = {}
	for index, word in enumerate(sentence):
		if word in fwords:
			if sdict.has_key(word):
				wordlist = sdict[word]
				wordlist.append(index)
				sdict[word] = wordlist
				#sdict[word] = float(sdict[word] + index) / 2
			else:
				sdict[word] = [index]
				
	for word in sdict:			
		total = sum(sdict[word])
		average = float(total) / len(sdict[word])
		sdict[word] = average
		
	indices.append(sdict)

#print indices

diffdict = {}

# loop over every sentence
# loop over the words in those sentences
# the first word should be the key for the first dictionary
# the value for that is -- a new dictionary yay!
# the first key in dict2 is the second word in the sentence
# the second key is the third word, etc
# the value for each key is the key word minus the dict word

for sentence in indices:
	words = sentence.keys()
	for index, word1 in enumerate(words):
		wordict = {}
		total = 0
		count = 0
		for word2 in words[index+1:]:
			wordict[word2] = abs(sentence[word2] - sentence[word1])
			total = total + wordict[word2]
			count = count + 1
			if diffdict.has_key(word1):
				if diffdict[word1].has_key(word2):
					diffdict[word1][word2] = float(total) / count
				else:
					diffdict[word1][word2] = wordict[word2]
			else:
				diffdict[word1] = wordict

pprint(diffdict)

# print prologue