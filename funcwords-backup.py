# Shakespeare analysis using functional words -- BACKUP

import re
import urllib2
from pprint import pprint
import itertools

fwords = urllib2.urlopen("https://fling.seas.upenn.edu/~maeisen/wiki/functionwords.txt").read().split(" ")

rawdata = open("tempest.txt").read().lower()
data = re.findall(r"[^.;:!?]+", rawdata)
data = [re.findall(r"[\w']+", item) for item in data]

indices = []

for sentence in data:
	sdict = {}
	for index, word in enumerate(sentence):
		if word in fwords:
			if sdict.has_key(word):
				wordlist = sdict[word]
				wordlist.append(index)
				sdict[word] = wordlist
			else:
				sdict[word] = [index]
		
	indices.append(sdict)

diffdict = {}

# loop over every sentence
# loop over the words in those sentences
# the first word should be the key for the first dictionary
# the value for that is -- a new dictionary yay!
# the first key in dict2 is the second word in the sentence
# the second key is the third word, etc
# the value for each key is the key word minus the dict word

# this function returns the difference between two words:

def getdistance(list1, list2):
	pairs = itertools.product(list1, list2)
	distances = [abs(t[0] - t[1]) for t in pairs]
	return distances

def average(list):
	total = sum(list)
	average = float(total) / len(list)
	return average

for sentence in indices:
	words = sentence.keys()
	for index, word1 in enumerate(words):
		wordict = {}
		for word2 in words[index+1:]:
			distances = getdistance(sentence[word1], sentence[word2])
			wordict[word2] = average(distances)
			diffdict[word1] = wordict

pprint(diffdict)


# 			if diffdict.has_key(word1):
# 				if diffdict[word1].has_key(word2):
# 					total = sum(diffdict[word1][word2])
# 					average = float(total) / len(diffdict[word1][word2])
# 					diffdict[word1][word2] = average
# 				else:
# 					diffdict[word1][word2] = wordict[word2]
# 			else:
# 				diffdict[word1] = wordict

# for sentence in indices:
# 	words = sentence.keys()
# 	for index, word1 in enumerate(words):
# 		wordict = {}
# 		total = 0
# 		count = 0
# 		for word2 in words[index+1:]:
# 			wordict[word2] = abs(sentence[word2] - sentence[word1])
# 			total = total + wordict[word2]
# 			count = count + 1
# 			if diffdict.has_key(word1):
# 				if diffdict[word1].has_key(word2):
# 					diffdict[word1][word2] = float(total) / count
# 				else:
# 					diffdict[word1][word2] = wordict[word2]
# 			else:
# 				diffdict[word1] = wordict
