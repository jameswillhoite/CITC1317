#!/bin/python
'''
Lab6b
Count vowels in the word, the number of letters, and percentage of vowels
James Willhoite
10/11/19
'''

word = raw_input("Enter a word: ")
vowels = ["a","e","i","o","u"]
found_vowels = []

for i in word:
	if i in vowels:
		found_vowels.append(i)




print "Letters: ", len(word)
print "Vowels: ", len(found_vowels)
percent = (len(found_vowels) * 1.0) / len(word)
print "Percentage of vowels: ", round(percent * 100, 2)


