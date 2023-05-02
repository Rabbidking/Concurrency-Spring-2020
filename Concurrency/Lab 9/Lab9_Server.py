import multiprocessing.connection
import random

address = ("127.0.0.1", 0x1234)	#opens port 1234 at address 127.0.0.1 (home address ---> we're running this program locally)
gameOver = False
board = [' '] * 9
turn = 'X'

#create the listener
listener = multiprocessing.connection.Listener(address, authkey = b"secretpasswd")

def drawBoard(board):
	print('   |   |')
	print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
	print('   |   |')

def isWinner(board, letter):
	#	6 | 7 | 8
	#	- + - + -
	#	3 | 4 | 5
	#	- + - + -
	#	0 | 1 | 2
	
	return((board[6] == letter and board[7] == letter and board[8] == letter) or			#top row
	(board[3] == letter and board[4] == letter and board[5] == letter) or					#middle row
	(board[0] == letter and board[1] == letter and board[2] == letter) or					#botom row
	(board[6] == letter and board[3] == letter and board[0] == letter) or					#left column
	(board[7] == letter and board[4] == letter and board[1] == letter) or					#middle column
	(board[8] == letter and board[5] == letter and board[2] == letter) or					#right column
	(board[6] == letter and board[4] == letter and board[2] == letter) or					#diagonal from top left to bottom right
	(board[8] == letter and board[4] == letter and board[0] == letter))						#diagonal from top right to bottom left

#accept multiple connections over and over again
while True:
	print("Waiting for connection 1...")
	c1 = listener.accept()
	print("Connection accepted from:", listener.last_accepted)
	print("Waiting for connection 2...")
	c2 = listener.accept()
	print("Connection accepted from:", listener.last_accepted)
	#both clients are now conected
	c1.send("You are 'Player 1' - You are 'X'")
	c2.send("You are 'Player 2' - You are 'O'")
	
	#we could have a loop that sends/receives...
	while gameOver == False:
		drawBoard(board)
		for i in range(8):
		
			if turn == 'X':
				c1.send('X')
				c1.send("Player 1, where do you want to move (number from 0-8)?")
				move = input()
				listener.recv(move)
				board[move] = turn
				if isWinner() == True:
					gameOver == True
					c1.send("You win!")
					c2.send("Player 1 wins!")
					break
				turn = 'O'
					
			else:
				c2.send("Player 1, where do you want to move (number from 0-8)?")
				move = listener.accept()
				board[move]
				if isWinner() == True:
					gameOver == True
					c1.send("You win!")
					c2.send("Player 1 wins!")
					break
				turn = 'X'

			drawBoard(board)
			
		c1.send("The game is a tie!")
		c2.send("The game is a tie!")
		c1.close()
		c2.close()