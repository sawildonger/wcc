
#need to use the random module
import random

print('Welcome to the Black Jack Game!')
#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

random.shuffle(cards)



#Round 1: 
print('Round 1:')
player_card1=cards.pop()
computer_card1=cards.pop()

print('Player card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))


#Round 2: 
#Option to hit or stay
print('Round 2:')
decision1 = raw_input("\nIf you want to stay type 's',if you want to hit type 'h':")

if decision1 == 'h':
	player_card2 = cards.pop()
	pc_info2 = str(player_card2)
	
else:
	player_card2 = 0
	pc_info2 = 'stay'


	
if computer_card1 < 10:
	computer_card2 = cards.pop()
	cc_info2 = str(computer_card2)
	
else:
	computer_card2 = 0
	print('Computer stays.')
	cc_info2 = 'stay'


print('Player cards: ' + str(player_card1)+ ' ' + pc_info2)
print('Computer cards: ' + str(computer_card1)+ ' ' + cc_info2)

	
	
#Round 3: 
#Option to hit or stay
print('Round 3:')
decision2 = raw_input("\nIf you want to stay type 's',if you want to hit type 'h':")

if decision2 == 'h':
	player_card3 = cards.pop()
	pc_info3 = str(player_card3)
else:
	player_card3 = 0
	pc_info3 = 'stay'

	
print('Player cards: ' + str(player_card1)+ ' ' + pc_info2 + ' ' + pc_info3)
	
if computer_card1 + computer_card2 < 16:
	computer_card3 = cards.pop()
	cc_info3 = str(computer_card3)
else:
	computer_card3 = 0
	cc_info3 = 'stay'


print('Computer cards: ' + str(computer_card1)+ ' ' + cc_info2 + ' '+ cc_info3)
	

player_total = player_card1 + player_card2 + player_card3
computer_total = computer_card1 + computer_card2 + computer_card3

print('Player total: ' + str(player_total))
print('Computer total: ' + str(computer_total))

if player_total > computer_total and player_total <= 21:
	print('Player wins!')
elif player_total < computer_total and computer_total <= 21:
	print('Computer wins!')
elif computer_total > 21 and player_total <= 21:
	print('Player wins!')
elif computer_total < 21 and player_total >= 21:
	print('Computer wins!')
elif computer_total > 21 and player_total > 21:
	print('Player and Computer have busted.')
else:
	print('Player and Computer have tied.')