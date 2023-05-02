import random
import multiprocessing

def cat(filename,pipeout):
	#function opens the file specified and loops by reads a line at a time,
	# then writing each to the pipe specified by pipeout.
	# once all lines have been read, the function should write None
	# to pipeout then terminate.
	file = open(str(filename), "r")
	lines = file.readlines()
	for l in lines:
		pipeout.send(l)
	pipeout.send(None)
	pipeout.close()
	file.close()

def grep(pattern,pipein,pipeout):
	#Loop
	# read a line from pipein
	# if the line read is None then write None to pipeout and terminate
	# if the pattern specified in contained in the line
	# then the line is written to pipeout.
	# lines not containing the pattern are discarded.
	while pipein:
		data = pipein.recv()
		if data == None:
			pipeout.send(None)
			return None
		elif data == pattern:
			pipeout.send(line)
		else:
			return None
	pipein.close()

def printer(pipein):
	#Loop
	# read a line
	# if the line is None then terminate
	# otherwise print the line out using print.
	line = pipein.recv()
	for l in line:
		if line == None:
			return None
		else:
			print(str(l))

if __name__ == '__main__':
	#create pipes
	pipein, pipeout = multiprocessing.Pipe()
	
	#create processes
	p1 = multiprocessing.Process(target=cat, args=("sonnets.txt", pipeout,))
	p2 = multiprocessing.Process(target=grep, args=("thee", pipeout, pipein,))
	p3 = multiprocessing.Process(target=printer, args=(pipein,))
	
	#start processes
	p1.start()
	p2.start()
	p3.start()
	
	#join processes
	p1.join()
	p2.join()
	p3.join()
	
	#enter to exit
	input("enter to exit")
	
	#cat("sonnets.txt",p1write)
	cat("sonnets.txt", pipeout)
	cat("thee", pipein)
    #cat("thee",p1read)