#!/bin/python
'''
James Willhoite
Lab6c 
10/16/19
'''

#Import the Random Module
import random
import time

num_rolls = 0
dice1 = 0
dice2 = 0
point = 0

def roll():
	global dice1, dice2, num_rolls
	num_rolls += 1
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)

while True:
	roll()
	print dice1, dice2
	sum = dice1 + dice2
	if num_rolls == 1:
		point = sum

	if num_rolls == 1 and sum in [7,11]: 
		print "Winner!"
		break
	elif num_rolls == 1 and sum in [2,3,12]:
		print "You Lose!"
		break
	
	if num_rolls > 1:
		if sum == 7:
			print "You lose!"
			break
		elif sum == point:
			print "You Win!"
			break



	time.sleep(1)

