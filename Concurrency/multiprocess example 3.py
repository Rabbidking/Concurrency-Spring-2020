import multiprocessing
import os
import random
import time


def myProcess(queue):
	print("Child PID is " , os.getpid())
	vote = random.choice(["Yes", "No"])
	queue.put(vote)
	time.sleep(random.uniform(1, 3))
	print("Child PID ", os.getpid(), " is done.")
	
if __name__ == "__main__":
	mainQueue = multiprocessing.Queue()

	processList = []
	for i in range(10):
		processList.append(multiprocessing.Process(target = myProcess, args = (mainQueue, )))
	
	print("Starting processes...")
	
	for process in processList:
		process.start()
	
	for process in processList:
		process.join()
	print("Processes done.")
	print("Gathering votes...")
	
	for i in range(10):
		vote = mainQueue.get()
		print("vote = " , vote)
	
	print("done")
	input("enter to exit")