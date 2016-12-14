# Shakespeare analysis using functional words

import re
import urllib2
from pprint import pprint
import itertools

fwords = urllib2.urlopen("https://fling.seas.upenn.edu/~maeisen/wiki/functionwords.txt").read().split(" ")

def getdistance(list1, list2):
	pairs = itertools.product(list1, list2)
	distances = [abs(t[0] - t[1]) for t in pairs]
	return distances

def average(list):
	total = sum(list)
	average = float(total) / len(list)
	return average

def finddiff(text):

	rawdata = open(text).read().lower()
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

	for sentence in indices:
		words = sentence.keys()
		for index, word1 in enumerate(words):
			for word2 in words[index+1:]:
				sdistances = getdistance(sentence[word1], sentence[word2])
				
				if diffdict.has_key(word1):
					if diffdict[word1].has_key(word2):
						diffdict[word1][word2].extend(sdistances)
					else:
						diffdict[word1][word2] = sdistances
				else:
					diffdict[word1] = {word2: sdistances}
	
	for word1 in diffdict:
		for word2 in diffdict[word1]:
			diffdict[word1][word2] = average(diffdict[word1][word2])
	
	return diffdict
	
test = finddiff("test2.txt")
tempest = finddiff("tempest.txt")

pprint(tempest)
