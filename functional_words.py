# Shakespeare analysis using functional words

import re
import urllib2

# fword = functional word

fwords = urllib2.urlopen("https://fling.seas.upenn.edu/~maeisen/wiki/functionwords.txt").read().split(" ")

# shakespeare = urllib2.urlopen("http://cs.stanford.edu/people/karpathy/char-rnn/shakespeare_input.txt").read().lower()

# shakes-naive-bayes/shakes_data/tempest.txt

data = open("test.txt").read().lower()
prologue = re.findall(r"[^.;:!?]+", data)
prologue = [re.findall(r"[\w']+", item) for item in prologue]

indices = []

for sentence in prologue:
	sdict = {}
	for index, word in enumerate(sentence):
		if word in fwords:
			if sdict.has_key(word):
				sdict[word] = float(sdict[word] + index) / 2
			else:
				sdict[word] = index
	indices.append(sdict)

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
	wordict = {}
	for index, word1 in enumerate(words):
		for word2 in words[index+1:]:
			wordict[word2] = sentence[word2] - sentence[word1]
			if diffdict.has_key(word1):
				if diffdict[word1].has_key(word2):
					diffdict[word1][word2] = float(diffdict[word1][word2] + wordict[word2]) / 2
				else:
					diffdict[word1][word2] = wordict[word2]
			else:
				diffdict[word1] = wordict

print diffdict

# print prologue