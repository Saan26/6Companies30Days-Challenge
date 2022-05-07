# group anagrams together ---------------------------

from collections import defaultdict


def printAnagramsTogether(words):
	groupedWords = defaultdict(list)

	# Put all anagram words together in a dictionary
	# where key is sorted word
	for word in words:
		groupedWords["".join(sorted(word))].append(word)
        
	# Print all anagrams together
	for group in groupedWords:
		print(" ".join(groupedWords[group]))


