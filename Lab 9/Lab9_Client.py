import multiprocessing.connection

address = ("127.0.0.1", 0x1234)	#opens port 1234 at address 127.0.0.1 (home address ---> we're running this program locally)
gameOver = False
board = [' '] * 9
turn = ''
i = 0

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
	(board[6] == letter and board[4] == letter and board[2] == letter)						#diagonal from top left to bottom right
	(board[8] == letter and board[4] == letter and board[0] == letter))						#diagonal from top right to bottom left



print("Connecting...")
connection = multiprocessing.connection.Client(address, authkey = b"secretpasswd")
print("Connected to:", address)

while True:
	#wait for data to come to us
	print("Waiting for data...")
	#receive data
	message = connection.recv()
	print("Message received:", message)
	
	while gameOver == False:
		drawBoard(board)
		for i in range(8):
			turn = connection.recv()
			turn_input = connection.recv()
			print(turn_input)
			move = input()
			connection.send(move)
		drawBoard(board)
	
	if gameOver == True:
		winMsg = connection.recv()
		input("enter to exit")
		print("Closing connection...")
		connection.close()
		print("Done!")