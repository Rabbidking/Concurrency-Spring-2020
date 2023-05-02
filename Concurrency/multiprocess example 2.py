import multiprocessing
import os
import random
import time

someGlobal = 0
q1 = multiprocessing.Queue()

def myProcess():
	global someGlobal
	someGlobal += 1
	print("Child added 1. Child PID is " , os.getpid())
	vote = random.choice(["Yes", "No"])
	q1.put(vote)
	time.sleep(random.uniform(1, 3))
	print("Child PID ", os.getpid(), " is done.")
	
if __name__ == "__main__":
	processList = []
	for i in range(10):
		processList.append(multiprocessing.Process(target = myProcess))
	#P1 = multiprocessing.Process(target = myProcess)
	#P2 = multiprocessing.Process(target = myProcess)
	
	print("Starting processes...")
	
	for process in processList:
		process.start()
	#P1.start()
	#P2.start()
	
	for process in processList:
		process.join()
	#P1.join()
	#P2.join()
	print("Processes done.")
	print("Gathering votes...")
	
	for i in range(10):
		vote = q1.get()
		print("vote = " , vote)
	
	print("someGlobal = " , someGlobal)
	print("done")
	input("enter to exit")