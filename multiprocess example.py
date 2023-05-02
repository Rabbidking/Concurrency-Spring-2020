import multiprocessing

someGlobal = 0

def myProcess():
	global someGlobal
	someGlobal += 1
	print("Child added 1")
	
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
	
	print("someGlobal = " , someGlobal)
	print("done")
	input("enter to exit")