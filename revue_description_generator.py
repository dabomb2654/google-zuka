from textblob import TextBlob
from textblob import Word
import sys
import pprint

#text = sys.stdin.read().lower()
#blob = TextBlob(text)
'''
print(type(blob.tags))
print(len(blob.tags))
NN_dict = {}
JJ_dict = {}
for word_type in blob.tags:
	#check type
	if 'NN' in word_type[1]:
		#print("got a noun")
		if word_type[0] in NN_dict.keys():
			#print(NN_dict[word_type[0]])
			NN_dict[word_type[0]] += 1
		else:
			NN_dict[word_type[0]] = 1
			#print("added", NN_dict[word_type[0]])
	if 'JJ' in word_type[1]: 
		#print("got an adj")
		if word_type[0] in JJ_dict.keys():
			#print(JJ_dict[word_type[0]])
			JJ_dict[word_type[0]] += 1
		else:
			JJ_dict[word_type[0]] = 1
			#print("added", JJ_dict[word_type[0]])

for key in NN_dict.keys():
	if NN_dict[key] >= 10:
		print(key, NN_dict[key])
print("/n")
for key in JJ_dict.keys():
	if JJ_dict[key] >= 10:
		print(key, JJ_dict[key])
'''
word = Word("star")
print(word.synsets)
