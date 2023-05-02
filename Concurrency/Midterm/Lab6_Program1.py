#John Bickel

import queue
import random
import threading
import time

snQueue = queue.Queue(maxsize = 100)
prodQueue = queue.Queue(maxsize = 100)
doneQueue = queue.Queue(maxsize = 100)

barrier1 = threading.Barrier(1)
barrier2 = threading.Barrier(1)

def serial_number():
	global value
	for i in range(0, 100):
		snQueue.put("Item:<" + str(i + 1) + ">")
	snQueue.put(None)

def production(producer_num):
	global value
	for i in range(0, 100):
		item = snQueue.get()
		if item == None:
			break
		else:
			time.sleep(random.uniform(.4, .5))
			production_string = str(item) + " Produced by #:<" + str(producer_num) + ">"
			prodQueue.put(production_string)
	barrier1.wait()
	prodQueue.put(None)

def packaging(packaging_num):
	global value
	for i in range(0, 100):
		item = prodQueue.get()
		if item == None:
			break
		else:
			time.sleep(random.uniform(.1, .2))
			packaging_string = str(item) +  " Packaged by #:<" + str(packaging_num) + ">"
			doneQueue.put(packaging_string)
	barrier2.wait()
	doneQueue.put(None)
	
def completion():
	global value
	for i in range(0, 100):
		item = doneQueue.get()
		if item == None:
			break
		else:
			print("Done: " + str(item))
	
t1 = threading.Thread(target = serial_number)
t2 = threading.Thread(target = production, args = (1,))
t3 = threading.Thread(target = packaging, args = (1,))
t4 = threading.Thread(target = completion)

time0 = time.time()
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
time1 = time.time()

print("Total time: " + str(time1 - time0))