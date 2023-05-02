#John Bickel

import queue
import random
import threading
import time

snQueue = queue.Queue(maxsize = 100)
prodQueue = queue.Queue(maxsize = 100)
doneQueue = queue.Queue(maxsize = 100)

barrier1 = threading.Barrier(8)
barrier2 = threading.Barrier(4)

def serial_number():
	global value
	for i in range(0, 100):
		snQueue.put("Item:<" + str(i + 1) + ">")
	for j in range(8):
		snQueue.put(None)

def production(producer_num):
	global value
	while True:
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
	while True:
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
	while True:
		item = doneQueue.get()
		if item == None:
			break
		else:
			print("Done: " + str(item))
			
threads = []
	
t1 = threading.Thread(target = serial_number)
threads.append(t1)
for i in range(8):
	t2 = threading.Thread(target = production, args = (i,))
	threads.append(t2)
for j in range(4):
	t3 = threading.Thread(target = packaging, args = (j,))
	threads.append(t3)
t4 = threading.Thread(target = completion)
threads.append(t4)

time0 = time.time()

for thread in threads:
	thread.start()
for thread in threads:
	thread.join()

time1 = time.time()

print("Total time: " + str(time1 - time0))