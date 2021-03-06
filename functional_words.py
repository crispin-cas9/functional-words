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

# for the compare_plays function, the arguments must be difference dictionaries.

def compare_plays(play1, play2):
	playdiff = {}
	for word1 in play1:
		if play2.has_key(word1):
			playdiff[word1] = {}
			for word2 in play1[word1]:
				if play2[word1].has_key(word2):
					playdiff[word1][word2] = abs(play1[word1][word2] - play2[word1][word2])

	return playdiff

tempest = finddiff("data/tempest.txt")
much_ado = finddiff("data/much_ado.txt")
macbeth = finddiff("data/macbeth.txt")
henryvi = finddiff("data/henry_vi_1.txt")
faustus = finddiff("data/faustus.txt")

temp_much_ado = compare_plays(tempest, much_ado)
temp_macbeth = compare_plays(tempest, macbeth)
temp_henryvi = compare_plays(tempest, henryvi)
temp_faustus = compare_plays(tempest, faustus)

# pprint(temp_much_ado)
