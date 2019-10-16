#!/bin/python

'''
Lab6a 
Find all Pythagorean Triples consisting of positive integers 
less than or equal to 20

James Willhoite
10/11/19
'''

found = []

max = 20
max += 1

for i in range(1,max):
	for j in range(1,max):
		for k in range(1,max):
			if (i**2 + j**2) == k**2:
				found.append([i,j,k])

print "Triples found are..."
print found

