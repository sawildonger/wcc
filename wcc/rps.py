import random

def check_move(move):
	if move == 'rock':
		return True
	elif move == 'paper':
		return True
	elif move == 'scissors':
		return True
	else:
		return False
		

def get_player_move():
	player_input = raw_input('Pick your move: rock, paper, or scissors?')
	while check_move(player_input) == False:
		print('Invalid move; pick again.')
		player_input = get_player_move()
	return player_input

def get_computer_move():
	a = ['rock','paper','scissors']
	random.shuffle(a)
	return a.pop()
	
def judge(moveA, moveB):
	if moveA == 'rock':
		if moveB == 'rock':
			outcome = 'Tie'
		elif moveB == 'scissors':
			outcome = 'A'
		elif moveB == 'paper':
			outcome = 'B'
	elif moveA == 'scissors':
		if moveB == 'rock':
			outcome = 'B'
		elif moveB == 'scissors':
			outcome = 'Tie'
		elif moveB == 'paper':
			outcome = 'A'
	elif moveA == 'paper':
		if moveB == 'rock':
			outcome = 'A'
		elif moveB == 'scissors':
			outcome = 'B'
		elif moveB == 'paper':
			outcome = 'Tie'
	return outcome

def play():
	print('Welcome to rock, paper, scissors!')

	playermove = get_player_move()
	
	computermove = get_computer_move()
	print('Computer chose: ' + computermove)
	
	comparison = judge(playermove, computermove)
		
	if comparison == 'A':
		print('Player has won!')
	elif comparison == 'B':
		print('Computer has won!')
	elif comparison == 'Tie':
		print('Player and Computer have tied!')
		
	play_again = raw_input('Play again? Type y or n: ')
	
	if(play_again=='y'):
		play()
	else:
		print('Thank you for playing!')
		
play()

