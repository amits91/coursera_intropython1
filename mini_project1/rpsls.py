# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
	""" Convert name to number """
	res = -1
	if name == 'rock':
		res = 0
	elif name == 'Spock':
		res = 1
	elif name == 'paper':
		res = 2
	elif name == 'lizard':
		res = 3
	elif name == 'scissors':
		res = 4
	else :
		print "Error: name_to_number(): invalid name ", name
	return res


def number_to_name(number):
	""" Convert number to name """
	res = 'Invalid Name'
	if number == 0:
		res = 'rock'
	elif number == 1:
		res = 'Spock'
	elif number == 2:
		res = 'paper'
	elif number == 3:
		res = 'lizard'
	elif number == 4:
		res = 'scissors'
	else :
		print "Error: number_to_name(): invalid number ", number
	return res
									
def rpsls(player_choice): 
	""" Rock-paper-scissors-lizard-Spock """
	# print a blank line to separate consecutive games
	print ""

	# print out the message for the player's choice
	print 'Player chooses', player_choice

	# convert the player's choice to player_number using the function name_to_number()
	player_number = name_to_number(player_choice)
	if player_number < 0 :
		return

	# compute random guess for comp_number using random.randrange()
	comp_number = random.randrange(0, 5)

	# convert comp_number to comp_choice using the function number_to_name()
	comp_choice = number_to_name(comp_number)

	# print out the message for computer's choice
	print 'Computer chooses', comp_choice

	# compute difference of comp_number and player_number modulo five
	diff = (comp_number - player_number) % 5

	# use if/elif/else to determine winner, print winner message
	if ((diff > 0) and (diff <= 2)):
		print "Computer wins!"
	elif ((diff > 2) and (diff <= 4)):
		print "Player wins!"
	elif (diff == 0):
		print "Player and computer tie!"
	else:
		print 'Error: rpsls(): Unable to decide for', player_choice

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


