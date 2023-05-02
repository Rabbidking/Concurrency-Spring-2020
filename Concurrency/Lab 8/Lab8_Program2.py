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

def wc(pipein,pipeout):
	#initialize a count variable to zero
	#Loop
	#read a line from pipein
	# if the line read is None then exit the loop
	# otherwise increment the count
	#after the loop, write the count to pipeout as a string: “Lines:”+str(count)
	#write None to pipeout and terminate
	
	count = 0
	while pipeout:
		data = pipein.recv()
		if data == None:
			return None
		else:
			count += 1
		pipeout.send("Lines: " + str(count))
	pipeout.send(None)
	return None

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

	pipe1, pipe2, pipe3 = multiprocessing.Pipe()
	
	p1 = multiprocessing.Process(target=cat, args=("sonnets.txt", pipe1,))
	p2 = multiprocessing.Process(target=grep, args=("thee", pipe1, pipe2,))
	p3 = multiprocessing.Process(target=wc,args=(pipe2, pipe3,))
	p4 = multiprocessing.Process(target=printer,args=(pipe3,))
	
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	
	input("enter to exit")