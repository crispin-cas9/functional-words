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
			wordict = {}
			for word2 in words[index+1:]:
				distances = getdistance(sentence[word1], sentence[word2])
				wordict[word2] = average(distances)
				diffdict[word1] = wordict
	
	return diffdict
	
	pprint(diffdict)
	
test = finddiff("test2.txt")
tempest = finddiff("tempest.txt")

print tempest
